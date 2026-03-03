Created: 2026-03-03 12:15
#quicknote

**Whois** is a query-response protocol (TCP port 43) used to retrieve domain registration records from public databases. It is one of the earliest steps in passive [[Information Gathering]], revealing registrant details, name servers, registration dates, and sometimes administrative contacts. In OSCP engagements, Whois helps map target ownership and identify related infrastructure before active scanning with [[Port scanning]].

- **What it reveals:** Registrant name and organisation, registrar, creation/expiration dates, name servers, and sometimes email addresses and phone numbers (if not behind privacy protection)
- **Usage:** `whois megacorpone.com` or `whois {IP_address}` for reverse lookups
- **Limitations:** Many registrations use WHOIS privacy services that mask real registrant data. Historical records can be accessed through services like DomainTools WHOIS History

## Resources

1. [ICANN WHOIS Lookup](https://lookup.icann.org/)
2. [DomainTools](https://www.domaintools.com/)

#### Tags
#oscp #reconnaissance #whois #cybersecurity #penetration_testing
