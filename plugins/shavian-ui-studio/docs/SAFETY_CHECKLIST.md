# Safety checklist for maintainers

Before every public release:

1. Run `bash scripts/test-local.sh`.
2. Run `claude plugin validate .`.
3. Run `claude plugin validate ./plugins/shavian-ui-studio`.
4. Inspect `git diff`.
5. Confirm there are no hooks, monitors, bundled MCP servers, credentials, or private files.
6. Confirm version numbers match.
7. Update `CHANGELOG.md`.
8. Regenerate `SHA256SUMS.txt`.
9. Tag the release.
