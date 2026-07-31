---
title: Refund API
type: API
version: 1.0
author: Admin
last_updated: 2026-07-29

tags:
  - refund
  - payment
  - billing

summary: API for initiating and managing customer refunds.
---

# Refund API

The Refund API is used to issue full or partial refunds for completed payments.

## Endpoint

POST /refunds

## Required Fields

- payment_id
- refund_amount
- reason

## Response

Returns

- refund_id
- status
- processed_at

## Possible Status

- Pending
- Processing
- Completed
- Failed

## Common Errors

- Payment Not Found
- Refund Window Expired
- Duplicate Refund Request

## Related

- [[Payment API]]
- [[Refund Policy]]
- [[Refund Process]]