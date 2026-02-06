# E-commerce Checkout Automation (API-First)

## Overview
This project demonstrates an **API-first automation framework** for testing an e-commerce checkout flow.

Backend APIs are used for **test setup and verification**, while the UI is used only for validating the **final checkout interaction**.  
The focus is on testing **real business workflows**, not isolated UI scripts.

---

## Design Principles

### API over UI wherever possible
Backend APIs are used to:
- create products
- manage cart state
- verify order creation

### UI only for true user interactions
The UI layer is used **only** to simulate a real user completing the checkout process.

---

## Responsibility Separation
Each layer has a single responsibility:

- **API Clients** → backend interactions and system state  
- **Page Objects** → UI behavior and user actions  
- **Tests** → orchestration and assertions  

This keeps tests readable, maintainable, and scalable.

---

## Authentication Strategy
Authentication is implemented using a **dual approach**:

### Stubbed Authentication (default)
- Used to keep tests deterministic and stable
- Allows tests to run without dependency on a live backend

### Real Authentication (optional)
- A real implementation using `requests.post()` is included
- Can be enabled when a live backend environment is available

This approach balances **reliability** with **realism**.

---

## Checkout Test Flow
The main end-to-end test validates a real business scenario:

1. Authenticate user (API – stubbed by default)
2. Create product (API)
3. Add product to cart (API)
4. Complete checkout (UI)
5. Verify order creation and status (API)

This ensures:
- fast test setup
- reliable assertions
- minimal UI dependency

---

## 📂 Project Structure

```
ecommerce-automation-framework/
├── api/
│   └── clients/
│       ├── auth_client.py
│       ├── product_client.py
│       ├── cart_client.py
│       └── order_client.py
│
├── ui/
│   └── pages/
│       ├── base_page.py
│       └── checkout_page.py
│
├── tests/
│   └── test_checkout_flow.py
│
├── conftest.py
├── pytest.ini
└── README.md
```


## Notes
- Payment gateway behavior is simulated
- Focus is on checkout logic and order validation
- Designed as a QA automation project, not a backend system