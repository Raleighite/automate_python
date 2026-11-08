# Understand this source

Open or download [the self-contained offline Floorplan](index.html). Search by a file or page name; use **Start here** for the guided tour and **Flows** for reviewed scenarios. The export has no cloud/Ask backend and does not run the source programs.

- Source commit: `742c32a9edecd22b911a9f255447e0823a31ead5`.
- 24 individually described files, 0 route cards, 6 plain-English groups, 2 flows and 5 tour stops; zero unassigned admitted code files.
- [Architecture, flows and tour](architecture.json), [file and route descriptions](descriptions/reviewed.json), [source and artifact provenance](source-manifest.json), [generator pins](generator.json), [notices](NOTICE.md).

## Source observations

Independent educational programs, not one integrated application. No HTTP routes. pw.py is an insecure source-backed clipboard exercise; three exact credential-literal spans were removed only in the private mapping derivative. Original source remains unchanged. Fixed classroom comparison strings are demonstration data, not live authentication.

All admitted code and configuration cards are described individually. Repository instructions, tests, Git/development metadata, environment files, lockfiles, original prose and binary/static artwork are not treated as application systems. Source-like config, lockfiles and original public assets are still freshness-pinned where selected by the policy below. Original licenses are unchanged. A source map is not deployment verification, runtime testing or security certification.

The route set is empty because these are standalone terminal scripts, not HTTP services. 

## Readability and navigation

At phone width, fit-to-view can make the graph overview small. Open **Start here**, search a named file/page and open its details, or play a flow to read normal-size prose. Use the details toggle if the phone sheet is closed, expand **More** for context, and zoom for graph labels. Measured initial overview label sizes are desktop: [13.92] effective px, mobile: [6.32] effective px. Opened descriptions, tour text and every flow note passed visible-ancestor, viewport geometry and at-least-13px prose checks. The overview itself is not generally phone-readable. Icon-only controls are less discoverable; physical pinch and assistive-technology behavior are not qualified by these desktop-emulated viewport tests. Source limitations above remain true even when the prototype UI uses optimistic wording.

## Check freshness

From repository root, using Python standard library and Git only:

```sh
python3 docs/floorplan/check_freshness.py
python3 -m unittest discover -s docs/floorplan/tests -v
python3 -O -m unittest discover -s docs/floorplan/tests -v
```

The checker compares RAW original source hashes and the complete tracked/unignored selected file set. It detects added, changed or deleted source, export drift and reviewed authoring/helper/notice drift. Its policy covers Python, JavaScript/TypeScript/JSX/TSX, HTML/CSS, SQL, TOML/YAML/JSON/INI, shell/C/C++ source, package/requirements files and all files under templates/static/public. It excludes docs, policies, tests, dependency/generated/cache trees and dot metadata. It never imports the application or silently renews pins. The tests copy actual source bytes into disposable Git fixtures and deliberately exercise rejection.

## Regeneration boundary

This repository contains the reviewed static export, authoring and pins, not the complete qualified generation runtime. Obtain and verify the exact reviewed runtime, full toolchain and already-present pinned image identified in generator.json; follow that runtime's REGENERATION.md. No internal catalog or operator-specific runtime location is required by these docs.

Prepare a fresh narrow regular-file source extraction from the pinned Git commit, omit development metadata before following any filesystem entries, and preserve RAW provenance. Renew the exact AST-literal-span credential derivative review recorded in source-manifest.json; never modify, print or feed the original credential literals into generation. Run the unchanged reviewed admit/scan and build/export path with `--include-reviewed`, author complete file/route descriptions, meaningful groups and real flows, and reconcile full owned implementation against actual admission. Do not weaken admission or substitute a partial map when a language, migration or route model is unsupported.

Review all prose against public source only. Preserve original licenses and the exact Floorplan/ELK/font notices. Test the exact installed HTML offline at desktop and phone widths, block external requests, search and open every file/route, traverse every tour/flow step, measure visible readable prose, run both freshness suites and deliberate coverage failures, and scan candidate docs plus the new commit range. Keep scans, raw caches and source records out of documentation. Local staging is not publication approval.
