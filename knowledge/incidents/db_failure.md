---
title: Database Failure
type: Incident

tags:
  - database

summary: Database unavailable.
---

# Database Failure

A database failure prevents normal application operations.

## Symptoms

- Login failure
- Slow response
- API errors

## Mitigation

- Fail over to replica.
- Restore latest backup.
- Notify engineering.

## Related

- [[Authentication API]]