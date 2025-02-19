# Version: MAJOR.MINOR.PATCH

Last Updated: 2025-02-19
__version__ = "0.0.1"

## Defensive Coding Best Practices

**Defensive Programming**: 
Write code that anticipates and handles potential errors or misuse. Validate inputs, handle exceptions gracefully, and ensure the system remains stable under unexpected conditions.

**Atomic Design Principles**:
- All procedure must adhere to the SRP (Single Responsibility Principle).
- Each component should have a single, well-defined responsibility.
- Components should be loosely coupled.
- Interfaces between components should be clearly defined.
- Functions should be small and focused.
- Classes should represent clear domain concepts.

**Component Design**
Each component should:
- Have a single responsibility.
- Be independently testable.
- Have clear interfaces.
- Be loosely coupled.
- Document its dependencies.

**Atomic Tests**: 
Write tests that are atomic, meaning each test should verify a single behaviour or responsibility. This makes it easier to identify the cause of a failure and ensures that tests are reliable and maintainable.

**Version Control Best Practices**:
- Use semantic versioning (MAJOR.MINOR.PATCH).
- Increment PATCH for bug fixes and minor changes.
- Increment MINOR for new features that maintain backward compatibility.
- Increment MAJOR for breaking changes.
- Document version changes in CHANGELOG.md.

**Documentation Standards**:
- Use clear and consistent section headers in CHANGELOG.md.
- Document not just what was changed, but why.
- Use "Addressing" section for attempted fixes rather than claiming solutions.
- Include file names in version headers when working with multiple files.
- Maintain history of attempted approaches and reversions.
- git commit commentary must reflect CHANGELOG.md update exactly.

**Testing Principles**:
- Write tests before implementing features (TDD).
- Keep mock objects simple and focused.
- Test both success and failure paths.
- Avoid testing multiple behaviours in a single test.
- Use appropriate fixtures to share common test setup.
- Comment test cases with clear descriptions of what is being tested.

**Refactoring Guidelines**:
- Document current responsibilities before refactoring.
- Plan atomic splits based on clear boundaries.
- Maintain backwards compatibility during migration.
- Test each atomic component independently.
- Validate integration points thoroughly.

**Error Handling**:
- Use specific exception types.
- Provide meaningful error messages.
- Log errors appropriately.
- Handle edge cases explicitly.

**Code Style**:
- Use consistent naming conventions.
- Follow language-specific style guides.
- Write self-documenting code with clear variable and function names.

**File Naming**:
- Use descriptive, specific filenames that indicate the component's purpose
- Avoid generic names like `manager.py` or `utils.py`
- Examples:
  - `session_manager.py` instead of `manager.py`
  - `pool_manager.py` instead of `manager.py`
  - `string_formatter.py` instead of `formatter.py`
  - `database_utils.py` instead of `utils.py`
- Test files should mirror source file names: `test_session_manager.py`

**Implementation Rules**:
- No circular imports.
- No business logic in entities.
- All computations based solely on internal state.
- Immutable where possible.
- Type hints throughout.
- Comprehensive docstrings classes and procedures.
- Input validation in constructors.

**Implementation Workflow**:
- Work on a single issue at a time.
    1. Update tests / Create test file.
    2. Implementation.
        - All updates/changes, should be focusing on a single issue at a time.
        - Updates should therefore only be made to a single procedure at a time.
    3. Run tests.
        - If test fails, fix implementation and repeat step 3.
        - If test passes, proceed to step 4.
    4. Generate CHANGELOG entry.
    5. Generate git staging and commit, commentary must match CHANGELOG.
        - Execute git staging and commit.
