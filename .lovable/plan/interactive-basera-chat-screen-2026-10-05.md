# Interactive Basera chat screen

Update only the chat section and its navigation integration; preserve the existing home, listings, account screens, branding, and Firebase settings.

- Add Hindi buying/selling tabs with a smoothly moving blue underline.
- Add all six requested quick filters in a horizontally scrollable row, with clear selection states.
- Show the exact requested Hindi empty-state text and buttons for each tab, plus a centered magnifying-glass character illustration.
- Connect “संदेश भेजना शुरू करें” to the existing home/listing view and “बेचना शुरू करें” to the existing listing form.
- Keep all five bottom navigation buttons visible and usable on the chat screen, with Chat highlighted.
- Test both tabs, all filters, both actions, bottom navigation, and existing conversation opening.

## Technical details
Keep the changes inside the existing embedded application. Filter existing conversations by buying/selling role and available unread, important, matched, and Elite flags, without inventing conversations or changing storage or messaging services.

## Reference and limitations
No OLX reference images are attached in this message, so match the written specifications rather than claim an exact image match. Existing chat messages are local demo conversations; this change does not add live messaging between users.