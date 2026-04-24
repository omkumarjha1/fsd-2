Name: Om Kumar Jha
Uid: 23BCC70012
Aim
To implement and compare different Token-based Authentication mechanisms in a Flask environment, specifically using standard Authorization headers, Custom headers, and JSON Web Tokens (JWT).

Procedure
Library Installation: Install PyJWT and Flask.

Basic Auth Setup: Create an endpoint that parses the request.authorization object sent via Postman's "Basic Auth" tab.

Custom Header Logic: Implement a route that manually checks for specific keys (e.g., X-Username) within the request.headers dictionary.

JWT Implementation:

Create a /login route that validates credentials and returns a signed encoded string (token).

Create a decorator (@token_required) to protect specific routes.

Verification: Use Postman to send requests with different header configurations and observe the status codes.

Learning Outcomes
Header Manipulation: Learn how to extract and validate data from various HTTP Request headers.

Stateless Authentication: Understand the benefits of JWT over session-based authentication for scalability.

Security Best Practices: Comprehend why "Bearer" tokens are the industry standard compared to sending plain-text credentials in custom headers.

Middleware/Decorators: Master the use of Python decorators to restrict access to sensitive API endpoints.

3. Postman Testing Guide (For your screenshots)
Basic Header: Go to the Auth tab -> Select Basic Auth -> Enter credentials. Postman automatically adds the Authorization header.

Custom Header: Go to the Headers tab -> Manually add X-Username and X-Password keys.

JWT/Bearer:

First, call /login to get the token.

Then, call /protected -> Auth tab -> Bearer Token -> Paste the generated token.

Since your campus drive is coming up, interviewers love asking about JWT structure (Header, Payload, Signature). Make sure you can explain why the secret key is vital for the signature part!