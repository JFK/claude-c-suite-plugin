---
description: QA Lead review — test coverage, quality metrics, testing strategy gaps
arguments:
  - name: scope
    description: "Focus area: 'full' (all tests), 'unit' (unit tests only), 'e2e' (E2E tests only), 'coverage' (coverage report), or a specific module path. Defaults to 'full'."
    required: false
---

Analyze the project's testing health from a QA Lead perspective.

## Steps

### 1. Gather current state

Run in parallel:
- Inventory test files: `find . -name '*.test.*' -o -name '*.spec.*' -o -name '*_test.*' | head -60`
- `gh issue list --state open --label "bug,test,flaky,regression" --json number,title,labels,milestone,createdAt` — open quality issues
- Check test config files (`vitest.config.*`, `jest.config.*`, `pytest.ini`, `playwright.config.*`, `Makefile`)
- Check CI config for test steps (`.github/workflows/`)
- `git log --oneline -20 -- '*.test.*' '*.spec.*' '*_test.*'` — recent test activity

If `$ARGUMENTS` provides a scope, narrow analysis to that area.

### 2. Test coverage inventory

Map test coverage across the codebase:

#### 2a. Backend coverage
- Which API endpoints have tests? Which don't?
- Are database operations (CRUD, migrations) tested?
- Are authentication/authorization flows tested?
- Are edge cases covered (invalid input, rate limits, concurrent access)?
- Are error paths tested, not just happy paths?

#### 2b. Frontend coverage
- Which components have unit tests?
- Are user interactions tested (click, input, form submit)?
- Are loading/error/empty states tested?
- Is routing tested?
- Are API integration points mocked and tested?

#### 2c. E2E coverage
- Which user flows have E2E tests?
- Do E2E tests cover critical paths (login, core CRUD, billing)?
- Are E2E tests stable or flaky?

### 3. Test quality assessment

For existing tests, evaluate:
- **Test isolation**: Do tests depend on each other or shared mutable state?
- **Assertion quality**: Are assertions specific enough? (`toBe` vs `toBeTruthy`)
- **Test naming**: Do test names describe behavior or just method names?
- **Fixture management**: Are test fixtures/factories well-organized?
- **Mock hygiene**: Are mocks minimal and realistic? Over-mocking hides bugs
- **Snapshot overuse**: Are snapshot tests used appropriately or as a lazy substitute?
- **Flaky tests**: Are there tests that pass/fail inconsistently?

### 4. Testing strategy gaps

Identify missing test categories:
- **Regression tests**: Are past bugs covered by tests to prevent recurrence?
- **Boundary tests**: Are edge cases (empty inputs, max lengths, special characters) tested?
- **Integration tests**: Are component interactions tested (not just units)?
- **Performance tests**: Are there load tests or performance benchmarks?
- **Security tests**: Are auth bypass, injection, and access control tested?
- **Accessibility tests**: Are a11y requirements verified in tests?

### 5. CI/CD quality gates

Evaluate the testing pipeline:
- **Test execution**: Are all tests run in CI? On every PR?
- **Coverage thresholds**: Are there minimum coverage requirements?
- **Failure policy**: Do test failures block merges?
- **Test speed**: How long do tests take? Are slow tests parallelized?
- **Flaky test handling**: Is there a process for quarantining flaky tests?

### 6. Apply QA Lead principles

1. **Test the contract, not the implementation** — Tests should verify behavior, not internal structure. If refactoring breaks tests without changing behavior, those tests are too coupled.
2. **Coverage is necessary but not sufficient** — 80% coverage with bad assertions is worse than 50% coverage with good ones. Quality over quantity.
3. **Every bug is a missing test** — When a bug is fixed, add a regression test. If bugs recur, the testing strategy has a gap.
4. **Fast feedback loop** — Unit tests should run in seconds, not minutes. Slow tests discourage running them.
5. **E2E tests are insurance, not proof** — They catch integration failures but are expensive. Don't duplicate unit-testable logic in E2E.
6. **Flaky tests erode trust** — A flaky test that's ignored is worse than no test. Fix or quarantine immediately.

### 7. Present findings

Structure output as:

```
## Testing Health Summary
- Overall health: [strong / adequate / gaps / undertested]
- Test file count: N (unit: N, integration: N, E2E: N)
- Estimated coverage: high/medium/low per area
- Open quality issues: N bugs, N flaky tests

## Coverage Map
| Area | Unit | Integration | E2E | Gaps |
|------|------|-------------|-----|------|
| Auth | Y/N | Y/N | Y/N | ... |
| API | Y/N | Y/N | Y/N | ... |
| UI | Y/N | Y/N | Y/N | ... |
| ... | ... | ... | ... | ... |

## Test Quality Issues
- [C] Critical: tests that give false confidence
- [W] Warning: quality issues that should be addressed
- [I] Info: improvement opportunities

## Untested Critical Paths
- List of features/flows with no test coverage that should have it
- Ranked by risk (user impact x likelihood of regression)

## CI/CD Assessment
- Pipeline coverage and speed
- Quality gate effectiveness
- Flaky test status

## Recommendations
- **Quick wins**: Easy tests to add for maximum coverage gain
- **Strategic gaps**: Areas needing systematic test investment
- **Process improvements**: CI/CD or workflow changes
- **Test infrastructure**: Tools or frameworks to adopt
```

### 8. Cross-reference with other views

If `/cto`, `/pm`, or `/cso` has been run in this session:
- Are high-debt areas also undertested? (compound risk)
- Are security-sensitive areas adequately tested?
- Do upcoming milestones include test work, or is it all features?

Do NOT execute any changes or write any tests. This is analysis only — recommend actions for the user to decide.
