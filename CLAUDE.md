# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository state

This repo currently contains no source code — only `ByteBites_Design_Reference.md` and this file. The git repo has no commits yet (branch `master`, no initial commit). Everything below describes the project that is about to be built, not code that exists.

## Project

ByteBites is a campus food ordering app. The work here is the **backend logic only**, written in plain Python classes and simple algorithms.

`ByteBites_Design_Reference.md` is the authoritative spec. Read it before making design decisions, and re-read it when scope is unclear — it is short and is expected to grow as the activity proceeds.

## Scope constraints (from the design reference)

These are hard boundaries, not preferences:

- No authentication logic.
- No database layer — keep state in memory, in Python data structures.
- No features that are not described in the spec.

When a request would cross one of these lines, say so and propose the in-scope alternative rather than building it.

## Behavioral instructions

`ByteBites_Design_Reference.md` has a **Behavioral Instructions** section that is still an empty HTML comment placeholder. Filling it in is part of the activity. Until the user writes it, ask rather than inventing conventions for class boundaries, complexity level, or how suggestions should be structured. Once it is filled in, treat it as an extension of this file.

## Tooling

No build, lint, test, or dependency configuration exists yet. Before introducing any of it (`requirements.txt`, `pyproject.toml`, `pytest`, a virtualenv), check with the user — for a CodePath tinker activity, plain `python3 <file>.py` on the standard library may be the intended setup.
