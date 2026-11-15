# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository state

The design is implemented. Run `python3 models.py` to run the demo scenario and its asserts. Files:

- `models.py`: the four classes, plus a demo under `if __name__ == "__main__":`.
- `test_bytebites.py`: pytest behavior tests. Run with `python3 -m pytest` (single test: `python3 -m pytest test_bytebites.py::test_name`).

- `bytebites_spec.md`: the client's feature request (what to build).
- `ByteBites_Design_Reference.md`: project scope and behavioral instructions (how to build it).
- `bytebites_design.mmd`: the approved Mermaid class diagram.

## Project

ByteBites is a campus food ordering app. The work here is the **backend logic only**, written in plain Python classes and simple algorithms.

Read `bytebites_spec.md` and `ByteBites_Design_Reference.md` before making design decisions, and re-read them when scope is unclear.

## Approved design

`bytebites_design.mmd` is the source of truth for class structure. Four classes, all linked by association ("has a"), with no inheritance:

- `MenuItem`: `name`, `price`, `category`, `popularity_rating`. Data only.
- `Menu`: `items: list[MenuItem]`; `add_item()`, `filter_by_category()`, `sort_by_popularity()` (returns a new list, highest rating first).
- `Order`: `items: list[MenuItem]`; `add_item()`, `compute_total()`. The spec calls this a "transaction", but the class is named `Order`.
- `Customer`: `name`, `purchase_history: list[Order]`; `add_purchase()`, `is_verified()`.

Design decisions made with the user:

- "Verify they are real users" means `is_verified()` returns True if `purchase_history` has at least one order. It is not auth.
- `purchase_history` stores whole `Order` objects, not loose items.
- `Order` does not reference `Customer`, so the link only goes one way.

If the code needs to diverge from the diagram, raise it with the user and update `bytebites_design.mmd` to match.

## Scope constraints

These are hard boundaries, not preferences:

- No authentication logic.
- No database layer: keep state in memory, in Python data structures.
- No features that are not described in the spec. IDs, quantities, tax/discounts, order status, and item removal were deliberately left out. Sorting by popularity was added at the user's request.

When a request would cross one of these lines, say so and propose the in-scope alternative rather than building it.

## Behavioral instructions

The **Behavioral Instructions** section of `ByteBites_Design_Reference.md` is filled in. Treat it as an extension of this file.

## Tooling

Tests use pytest, which the activity asks for and which is already installed. The code itself is standard library only. There is no `requirements.txt`, `pyproject.toml`, lint config, or virtualenv. Check with the user before adding any of those.
