# Testing of API routes

Here are the test results for the different API endpoints and their expected results.

## **TABLE OF CONTENTS**

[**Base Route**](#base-route)

[**Categories**](#categories)

[**Comments**](#comments)

[**Followers**](#followers)

[**Hacks**](#hacks)

[**Profiles**](#profiles)

[**Ratings**](#ratings)

---

## **Base Route**

| Test | Expected Result | Result |
|------|-----------------|--------|
| Enter `/` route | "Connection to Hack Collect API successful." message should appear | Pass |

---

## **Categories**

| Test | Expected Result | Result |
|------|-----------------|--------|
| Enter the `/categories/` route | All data needed should be displayed | Pass |
| Check for amount of entries in response | Number of entries for the given route should be displayed | Pass |
| Check for possible next page of pagination | Should be null if none is present or link to the next page when more than 10 entries are there | Pass |
| Check for possible previous page of pagination | Should be null if none is present or link to the last page when more than 10 entries are there and the next page was called | Pass |
| Check results object | A list of all entries should be displayed with all attributes given in the DRF setup | Pass |
| Enter the `/categories/id/` route with a valid entry | Only a single entry should be displayed | Pass |
| Enter the `/categories/id/` route with an invalid entry | detail: "No Category matches the given query." should appear | Pass |

---

## **Comments**

| Test | Expected Result | Result |
|------|-----------------|--------|
| Enter the `/comments/` route | All data needed should be displayed | Pass |
| Check for amount of entries in response | Number of entries for the given route should be displayed | Pass |
| Check for possible next page of pagination | Should be null if none is present or link to the next page when more than 10 entries are there | Pass |
| Check for possible previous page of pagination | Should be null if none is present or link to the last page when more than 10 entries are there and the next page was called | Pass |
| Check results object | A list of all entries should be displayed with all attributes given in the DRF setup | Pass |
| Enter the `/comments/id/` route with a valid entry | Only a single entry should be displayed | Pass |
| Enter the `/comments/id/` route with an invalid entry | detail: "No Category matches the given query." should appear | Pass |
| Check for annotated fields or custom entries specified in the DRF | Additional fields should be displayed | Pass |

---

## **Followers**

| Test | Expected Result | Result |
|------|-----------------|--------|
| Enter the `/followers/` route | All data needed should be displayed | Pass |
| Check for amount of entries in response | Number of entries for the given route should be displayed | Pass |
| Check for possible next page of pagination | Should be null if none is present or link to the next page when more than 10 entries are there | Pass |
| Check for possible previous page of pagination | Should be null if none is present or link to the last page when more than 10 entries are there and the next page was called | Pass |
| Check results object | A list of all entries should be displayed with all attributes given in the DRF setup | Pass |
| Enter the `/followers/id/` route with a valid entry | Only a single entry should be displayed | Pass |
| Enter the `/followers/id/` route with an invalid entry | detail: "No Category matches the given query." should appear | Pass |

---

## **Hacks**

| Test | Expected Result | Result |
|------|-----------------|--------|
| Enter the `/hacks/` route | All data needed should be displayed | Pass |
| Check for amount of entries in response | Number of entries for the given route should be displayed | Pass |
| Check for possible next page of pagination | Should be null if none is present or link to the next page when more than 10 entries are there | Pass |
| Check for possible previous page of pagination | Should be null if none is present or link to the last page when more than 10 entries are there and the next page was called | Pass |
| Check results object | A list of all entries should be displayed with all attributes given in the DRF setup | Pass |
| Enter the `/hacks/id/` route with a valid entry | Only a single entry should be displayed | Pass |
| Enter the `/hacks/id/` route with an invalid entry | detail: "No Category matches the given query." should appear | Pass |
| Check for annotated fields or custom entries specified in the DRF | Additional fields should be displayed | Pass |

---

## **Profiles**

| Test | Expected Result | Result |
|------|-----------------|--------|
| Enter the `/profiles/` route | All data needed should be displayed | Pass |
| Check for amount of entries in response | Number of entries for the given route should be displayed | Pass |
| Check for possible next page of pagination | Should be null if none is present or link to the next page when more than 10 entries are there | Pass |
| Check for possible previous page of pagination | Should be null if none is present or link to the last page when more than 10 entries are there and the next page was called | Pass |
| Check results object | A list of all entries should be displayed with all attributes given in the DRF setup | Pass |
| Enter the `/profiles/id/` route with a valid entry | Only a single entry should be displayed | Pass |
| Enter the `/profiles/id/` route with an invalid entry | detail: "No Category matches the given query." should appear | Pass |
| Check for annotated fields or custom entries specified in the DRF | Additional fields should be displayed | Pass |

---

## **Ratings**

| Test | Expected Result | Result |
|------|-----------------|--------|
| Enter the `/ratings/` route | All data needed should be displayed | Pass |
| Check for amount of entries in response | Number of entries for the given route should be displayed | Pass |
| Check for possible next page of pagination | Should be null if none is present or link to the next page when more than 10 entries are there | Pass |
| Check for possible previous page of pagination | Should be null if none is present or link to the last page when more than 10 entries are there and the next page was called | Pass |
| Check results object | A list of all entries should be displayed with all attributes given in the DRF setup | Pass |
| Enter the `/ratings/id/` route with a valid entry | Only a single entry should be displayed | Pass |
| Enter the `/ratings/id/` route with an invalid entry | detail: "No Category matches the given query." should appear | Pass |