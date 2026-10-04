"""Wire Basera icons into an EXISTING Android project; never create an app ID.

Usage: python3 scripts/install-android-icons.py /path/to/existing/android
The target must contain app/src/main/AndroidManifest.xml and app/build.gradle(.kts).
"""
from pathlib import Path
import argparse
import re
import shutil
import xml.etree.ElementTree as ET

ANDROID_NS = "http://schemas.android.com/apk/res/android"


def install(android_root: Path) -> None:
    main = android_root / "app/src/main"
    manifest_path = main / "AndroidManifest.xml"
    if not manifest_path.is_file() or not any(
        (android_root / "app" / name).is_file()
        for name in ("build.gradle", "build.gradle.kts")
    ):
        raise SystemExit("An existing Android app is required; no project was created or changed.")

    text = manifest_path.read_text()
    tree = ET.fromstring(text)
    app = tree.find("application")
    if app is None:
        raise SystemExit("AndroidManifest.xml has no application element; nothing was changed.")
    if not re.search(r'xmlns:android\s*=\s*[\"\']' + re.escape(ANDROID_NS), text):
        raise SystemExit("Expected Android namespace declaration; nothing was changed.")
    # Aliases/activity overrides can supersede application icons. Refuse ambiguous wiring.
    if any(
        node.get(f"{{{ANDROID_NS}}}{key}") is not None
        for node in app.iter()
        if node is not app
        for key in ("icon", "roundIcon")
    ):
        raise SystemExit("Activity/alias icon overrides need review; nothing was changed.")

    match = re.search(r"<application\b[^>]*>", text, re.S)
    if match is None:
        raise SystemExit("Cannot locate application tag; nothing was changed.")
    tag = match.group(0)
    for key, value in (("icon", "@mipmap/ic_launcher"), ("roundIcon", "@mipmap/ic_launcher_round")):
        pattern = r"android:" + key + r"\s*=\s*([\"\']).*?\1"
        replacement = f'android:{key}="{value}"'
        if re.search(pattern, tag, re.S):
            tag = re.sub(pattern, replacement, tag, flags=re.S)
        else:
            tag = tag[:-1] + f"\n        {replacement}>"
    updated = text[:match.start()] + tag + text[match.end():]
    parsed = ET.fromstring(updated)
    if parsed.get("package") != tree.get("package"):
        raise SystemExit("Package identity changed unexpectedly; nothing was changed.")
    source = Path(__file__).resolve().parents[1] / "platform-assets/android/res"
    if not source.is_dir():
        raise SystemExit("Basera Android icon resources are missing; nothing was changed.")
    backup = manifest_path.with_name("AndroidManifest.xml.before-basera-icons")
    if not backup.exists():
        shutil.copy2(manifest_path, backup)
    for asset in source.rglob("*"):
        if asset.is_file():
            destination = main / "res" / asset.relative_to(source)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(asset, destination)
    manifest_path.write_text(updated)
    print("Connected Basera icon and roundIcon in the existing AndroidManifest.xml.")
    print("Copied density-specific legacy/adaptive resources; application ID and Gradle files unchanged.")
    print("Build variant overlays and the final APK/AAB must still be verified in the actual Android project.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("android_project", type=Path)
    install(parser.parse_args().android_project.resolve())