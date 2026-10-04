# Maintainer Merge Checklist

Use this checklist when reviewing a pull request that adds or modifies an Atlas resource. Keep the review focused on correctness, safety, attribution, and long-term maintainability.

## Before approval

- [ ] **Scope:** The PR has one coherent purpose and the resource belongs in the Atlas.
- [ ] **Structure:** Files use the documented resource type, directory, naming, and metadata conventions.
- [ ] **Quality:** The resource is clear, reusable, appropriately scoped, and includes useful examples or expected outputs where applicable.
- [ ] **Duplication:** Existing resources were checked; intentional variants are clearly differentiated.
- [ ] **Validation:** `python scripts/validate_atlas.py` passes.
- [ ] **Tests:** Relevant tests pass, and new validation behavior has regression coverage when needed.
- [ ] **Safety:** No secrets, private data, malicious payloads, unsafe defaults, or instructions intended to compromise unrelated users/tools are introduced.
- [ ] **Attribution:** External or adapted material has appropriate source, license, and attribution information. See [Licensing & Attribution](licensing-and-attribution.md).
- [ ] **Documentation:** Contributor-facing behavior, schema changes, or new workflows are documented where needed.
- [ ] **Generated files:** Catalog or generated outputs are updated using the project's tooling when the change requires it.

## Before merging

- [ ] CI is passing and any failures are understood.
- [ ] Requested changes and reviewer questions have been addressed.
- [ ] The final diff contains no unrelated changes.
- [ ] Contributor feedback has been acknowledged or a clear follow-up has been recorded.

## Related policies

- [CONTRIBUTING.md](../CONTRIBUTING.md)
- [SECURITY.md](../SECURITY.md)
- [Licensing & Attribution](licensing-and-attribution.md)

> This checklist supports consistent review; maintainers should still use judgment for unusual contributions or security-sensitive changes.
