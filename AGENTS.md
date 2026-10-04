<!-- LOVABLE:BEGIN -->
> [!IMPORTANT]
> This project is connected to [Lovable](https://lovable.dev). Avoid rewriting
> published git history — force pushing, or rebasing/amending/squashing commits
> that are already pushed — as it rewrites history on Lovable's side and the
> user will likely lose their project history.
>
> Commits you push to the connected branch sync back to Lovable and show up in
> the editor, so keep the branch in a working state.
<!-- LOVABLE:END -->

## Icon architecture
- Generate platform icons from the unchanged uploaded source in `assets/branding/basera-original.png`; keep framing-only derivatives separate so branding is never reconstructed.
- Connect web icons in both the TanStack root head and the standalone embedded HTML head so either entry uses identical assets.
- Keep native icon resources under `platform-assets/android/res` until an existing Android project is supplied; never invent a package ID or claim native build wiring without that project.
- Use the guarded installer in `scripts/install-android-icons.py` to wire resources into an existing Android manifest without changing application identity.
