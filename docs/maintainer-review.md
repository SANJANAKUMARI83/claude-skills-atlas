# Maintainer Review Guide

Review every contribution for:

- **Usefulness:** solves a real, repeatable task.
- **Structure:** clear purpose, inputs, process, outputs, and limitations where relevant.
- **Originality:** no copied third-party prompt collections or incompatible licenses.
- **Scope:** one focused resource per file or directory.
- **Safety:** no secrets, credential requests, malware, or deceptive instructions.
- **Verification:** examples and tests are included when practical.
- **Portability:** avoid unnecessary dependence on one private project.

### PR checklist

- [ ] Resource type and location are correct.
- [ ] Metadata is valid when supplied.
- [ ] Instructions are deterministic enough to reuse.
- [ ] Links resolve.
- [ ] Examples are realistic.
- [ ] Catalog is generated or CI can regenerate it.
- [ ] Attribution/licensing is clear.

Request changes when a resource fails a core quality or safety requirement. Merge when the checklist is satisfied and CI passes.
