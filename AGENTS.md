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

## Embedded chat screen
- Keep the marketplace chat list and its synchronous tab/filter state in the embedded Basera application, reusing existing navigation and listing actions so the original screens and local messaging remain intact.
- Treat missing chat roles as buying and filter only explicit conversation metadata; never fabricate sellers, unread messages, or Elite status to populate filters.

## Language preference
- Persist the UI language only from an explicit language-menu choice under its dedicated storage key, never from startup rendering, so the English default can't be overwritten by an automatic save.
- Render all chat-list text through the shared `t()` translations and `data-i18n` attributes so it changes along with the global language.

## Header and wishlist
- Render header tools and wishlist through React portals into the embedded document; use document events for language, navigation, and favorites so the existing application remains intact.
- Keep wishlist selections in React session state and mirror selection IDs to embedded listing controls; no backend or persistent storage is needed for this session-only feature.
