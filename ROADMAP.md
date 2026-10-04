# Claude Skills Atlas Roadmap

The Atlas is evolving from a collection of reusable AI resources into a reliable, searchable resource layer for modern agent workflows.

> **Roadmap status:** priorities can change as the project, community feedback, and agent ecosystem evolve. Issues linked below are the current implementation backlog, not fixed commitments.

## Near-term — Foundation and contributor experience

These are the highest-priority improvements for making contributions easier to validate, discover, and maintain.

- [ ] **Versioned skill specification and metadata schema** — define a consistent contract for skills and future resource types. ([#108](https://github.com/cellrishi-code/claude-skills-atlas/issues/108))
- [ ] **Automated skill validation and linting** — catch malformed resources and broken references in pull requests. ([#109](https://github.com/cellrishi-code/claude-skills-atlas/issues/109))
- [ ] **Machine-readable skill registry** — generate a canonical discovery index for agents and integrations. ([#110](https://github.com/cellrishi-code/claude-skills-atlas/issues/110))
- [ ] **Security and trust guidelines** — establish review expectations for third-party and agent-executable resources. ([#111](https://github.com/cellrishi-code/claude-skills-atlas/issues/111))
- [ ] **Cross-agent compatibility metadata** — document portability across Claude Code, Codex, and other agent environments. ([#112](https://github.com/cellrishi-code/claude-skills-atlas/issues/112))
- [ ] **Contributor workflow** — provide a predictable path from idea to tested, reviewable pull request. ([#113](https://github.com/cellrishi-code/claude-skills-atlas/issues/113))

### How to contribute

- **New contributor:** choose an issue labeled for contribution, improve one resource, or add a focused skill/prompt using the templates.
- **Developer/tooling contributor:** work on validation, registry generation, CI, or compatibility metadata.
- **Reviewer/maintainer:** help review resources against quality and security criteria.
- **Domain contributor:** propose or improve resources in an area where you have practical expertise.

For any contribution, start with the relevant issue, make the smallest focused change, test it where practical, and open a pull request explaining the problem and verification performed.

## Medium-term — Quality, scale, and maintainability

Once the foundation is stable, the focus shifts toward making a growing community library easier to evaluate and maintain.

- [ ] **Skill quality tiers and review criteria** — make maturity and reliability visible to users. ([#114](https://github.com/cellrishi-code/claude-skills-atlas/issues/114))
- [ ] **Duplicate and overlapping skill detection** — reduce fragmentation as the library grows. ([#115](https://github.com/cellrishi-code/claude-skills-atlas/issues/115))
- [ ] Expand automated Markdown and link validation.
- [ ] Improve catalog generation and resource discoverability.
- [ ] Add more domain maintainers as the project grows.
- [ ] Build a broader, high-quality contributor base across disciplines.
- [ ] Establish recurring community contribution drives and highlight notable contributions.

## Exploratory — Agent ecosystem and distribution

These ideas are intentionally less committed and will be evaluated based on adoption, maintenance cost, and community demand.

- [ ] Expand Claude Code plugin capabilities.
- [ ] Improve the ChatGPT-compatible integration and deployment guidance.
- [ ] Develop Codex and additional agent integrations.
- [ ] Explore a static website for browsing, filtering, and copying resources.
- [ ] Explore richer semantic search and resource recommendation.
- [ ] Explore automated quality signals derived from usage and review data.

## Success criteria

The roadmap is successful when the Atlas becomes easier to:

1. **Discover** — people and agents can find the right resource quickly.
2. **Trust** — users can understand quality, compatibility, safety, and limitations.
3. **Contribute** — contributors have clear tasks, conventions, and review paths.
4. **Reuse** — resources can move across supported agent environments.
5. **Maintain** — automation prevents quality regressions as the repository scales.

Priorities may be reordered, removed, or replaced as the project develops. Community feedback and real-world usage should guide those decisions.

## Contribution principle

**Quality comes before quantity.** The goal is not to manufacture activity or copy large prompt collections. The goal is to build a genuinely useful, well-attributed library that people return to and contribute to.
