# The DelightQL Query Language

- **URL:** https://delightql.org
- **Author:** delightql.org by reverendpaco
- **Published Date:** 2026-10-14 18:41 UTC
- **Tags:** `databases`, `sql`
- **Source:** Lobste.rs (Databases)

---

## Summary
Hey all, I would like to present a programming language I have been developing for many years called delightql. This is an alpha release so there will be rough edges, but I have used it at home and work and have liked it enough to now throw it out into the world and see if it sticks. It's always a good thing if you like the language you've developed. Delightql transpiles to SQL and looks something like a cross between Prolog, Elixir and cough Perl. I will try now to enumerate some features: reusable functions, reusable higher-order predicates, reusable row-predicates 99% of all SQL (this is a vibe estimation and not a guarantee) some stuff you never knew you wanted (union corresponding, anonymous tables, tree-groups, the occassional prolog-like join) ETL directives and a module system Coding in delightql will feel like a concatenative language insofar as the meaning of the query is explicitly read from left to right. The language is implemented in Rust and is Apache licensed. I used LLMs over the past year and a half to help me with the implementation. The design (syntax, semantics, and features) is all my own work. To that last point, I note that out of pure happenstance my mode of working was exactly suited to this new world of LLMs. Back in 2020 I decided to stop implementing and just write. By 2025, I had finished writing the book about the language I wanted. I'd love to hear what makes sense, what doesn't, and/or kudos/criticisms. Comments
