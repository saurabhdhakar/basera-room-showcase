import { createFileRoute } from "@tanstack/react-router";
import { useState } from "react";
import { WishlistNavigation } from "@/components/WishlistNavigation";

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
  const [embeddedDocument, setEmbeddedDocument] = useState<Document | null>(null);
  return (
    <>
    <iframe
      src="/basera.html"
      title="Basera"
      className="fixed inset-0 h-full w-full border-0"
      onLoad={(event) => setEmbeddedDocument(event.currentTarget.contentDocument)}
    />
    {embeddedDocument && <WishlistNavigation document={embeddedDocument} />}
    </>
  );
}
