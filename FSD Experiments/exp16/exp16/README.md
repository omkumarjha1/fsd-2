Name: Om Kumar Jha
UID: 23BCC70012
# Experiment 16: Unit Testing for Frontend and Backend

This folder contains a small Flask backend and a Vite + React frontend to demonstrate unit testing.

## Backend Testing
- File: `app.py`
- Test file: `test_app.py`
- Tooling: `pytest`, `pytest-cov`

### Run backend tests
- `pytest -v`
- `pytest test_app.py`
- `pytest test_app.py::test_create_student`
- `pytest --cov=app --cov-report=term-missing --cov-report=html`

## Frontend Testing
- Component: `src/components/Form.jsx`
- Test file: `src/components/Form.test.jsx`
- Tooling: `vitest`, `@testing-library/react`, `@testing-library/jest-dom`, `jsdom`

### Run frontend tests
- `npx vitest`
- `npx vitest run`
- `npx vitest run --coverage`

## Notes
- Backend uses in-memory student storage for testing.
- Frontend form validates password length and shows an error for short passwords.
