---
headline: "An invoice hub where AI reads and a person approves"
client: "Out There Outfitters"
clientUrl: "https://www.outthereoutfitters.com"
summary: "Vendor bills were landing in QuickBooks wrong and getting retyped by hand. Now AI reads each invoice, someone at the store approves the match, and only then does anything touch the books."
track: production
order: 2
stack: ["Python", "Claude", "QuickBooks API", "Lightspeed", "Shopify Flow"]
image: "/images/work/oto-invoices.png"
imageAlt: "The invoice hub: forward an invoice or add the PDF, approve the match, and anything unfinished waits under Needs you."
approved: false
---

## The problem

When the store's point-of-sale system creates a bill in QuickBooks, three things come in wrong: the invoice number, a due date 10 days out, and no payment terms. Someone had to open each vendor PDF and retype them. That was about 140 bills a month.

It's not just busywork. Until a bill is fixed, the cash-flow report shows it due in 10 days instead of 30 to 90, so the store was planning around the wrong numbers.

## What we built

A hub that reads each vendor invoice and lines it up with the right bill.

1. **AI reads the PDF.** That's all it does. It never decides on its own.
2. **A bill matches only on an exact PO match.** There's no guessing from product names.
3. **A person at the store approves, corrects, or rejects each match.** Nothing is written to QuickBooks without that OK.
4. **It writes four fields only:** invoice number, invoice date, payment terms, and due date. It never touches amounts or line items.

## What makes it production

- **Practice mode first.** Before anything went live, the store tried it on sample invoices against a pretend QuickBooks. Approve saved their OK, and nothing else happened.
- **It won't overwrite a person.** If someone edited the bill in QuickBooks in the meantime, the write is refused.
- **Trust is earned per vendor.** A brand can switch to automatic only after 20 matches in a row are approved unchanged, plus an explicit switch. One correction resets the count. So far every brand is still in review, by choice.
- **It fixes itself, carefully.** Every 30 minutes, Claude looks at anything stuck and proposes a fix. Plain code checks each fix before it's applied, and the store gets one email per run.

## Results

The first invoice came in Oct 18, 2026. Writing to QuickBooks started Oct 26. Through Nov 5:

- **251 PDFs came in.** 28 were statements, order confirmations, or flyers and got set aside on their own. The rest were read as invoices, from 47 brands.
- **80 written to QuickBooks**, every one approved first: 63 existing bills filled in with the invoice details, and 17 new bills created.
- **14 closed on their own**, because the bill was already handled in QuickBooks.

> "The invoice part of the hub is fantastic!"
>
> Heidi, Out There Outfitters

## Same store, same idea: an order hold

Three canceled orders had been headed to freight forwarders, all from first-time customers. Shopify's fraud check looks at the card, not the address.

So we added a Shopify Flow that holds orders like that, tags them for review, and emails the store before anything ships. It went live Nov 1.
