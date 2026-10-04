import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title: "Basera — Rooms & Flats, All India" },
      { name: "description", content: "Find and list rooms, flats and PGs across India with Basera." },
      { property: "og:title", content: "Basera — Rooms & Flats, All India" },
      { property: "og:description", content: "Find and list rooms, flats and PGs across India with Basera." },
      { property: "og:type", content: "website" },
      { name: "twitter:card", content: "summary_large_image" },
    ],
  }),
  component: Index,
});

function Index() {
  return (
    <iframe
      src="/basera.html"
      title="Basera"
      className="fixed inset-0 h-full w-full border-0"
    />
  );
}
