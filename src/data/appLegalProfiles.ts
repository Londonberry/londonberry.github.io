export interface AppLegalProfile {
  slug: string;
  name: string;
  legalProvider: string;
  contactEmail: string;
  location: string;
  effectiveDate: string;
  appDescription: string;
  dataPurpose: string;
  quickBooksDataDescription: string;
}

export const appLegalProfiles: AppLegalProfile[] = [
  {
    slug: 'londonberry-oto-cash-flow',
    name: 'Londonberry OTO Cash Flow',
    legalProvider: 'Londonberry',
    contactEmail: 'info@londonberry.com',
    location: 'Jacksonville, Florida, United States',
    effectiveDate: 'April 28, 2026',
    appDescription:
      'an internal business reporting tool that connects authorized QuickBooks Online companies to cash-flow reports and related operational reporting workflows for end users designated by the customer.',
    dataPurpose:
      'generate and deliver authorized reports, synchronize authorized accounting information, maintain the QuickBooks Online connection, secure the service, troubleshoot user requests, improve reliability, and comply with legal obligations.',
    quickBooksDataDescription:
      'company profile details and accounting records needed for the App\'s cash-flow workflows, such as customers, vendors, invoices, bills, payments, accounts, items, transactions, reports, balances, and related metadata, depending on the scopes approved by the user.',
  },
];
