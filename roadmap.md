# Basera icon optimization

- [x] Generate web, Apple, maskable, Android-density and Play Store icons from the unchanged uploaded logo.
- [x] Connect and verify all web icon references without changing UI or Firebase settings.
- [x] Prepare native Android resources and an installer for an existing Android project.
- [x] Deliver icon inventory and verification report.
- [ ] Verify actual Android launcher/build wiring — blocked: this repository has no Android/Capacitor project or existing application ID.

## Interactive Hindi chat screen
- [x] Add buying/selling tabs, quick filters, illustration, and exact Hindi empty states.
- [x] Connect primary actions and keep all five bottom navigation items usable.
- [x] Verify tab/filter/action interactions and preserve existing messaging behavior.

## Language preference and chat translations
- [x] Default first launch to English and persist Hindi only after an explicit language selection.
- [x] Ignore Hindi values auto-saved by the old startup logic so existing devices also open in English.
- [x] Translate every chat-list label and empty state from the global language state without changing handlers.
- [x] Verify first launch, saved language reload, instant language switching, and chat interactions.

## Header and wishlist
- [x] Add microphone, favorites, and notification controls beside search.
- [x] Add React session-state wishlist with translated empty state, saved listings, and working return actions.
- [x] Verify navigation, session favorite add/remove, touch feedback, and language synchronization; live property data and microphone permission remain dependent on configured Firebase and browser support.
## Pre-home sign-in flow
- [ ] Add the Basera welcome and email/social sign-in experience before the existing marketplace home.
- [ ] Check the managed account session on launch and keep the marketplace behind the sign-in flow.
- [ ] Save a user-owned profile on account creation without altering chat, wishlist, or embedded Firebase behavior.
- [ ] Verify welcome, sign-in, signup confirmation, authenticated entry, and existing home navigation.
