// Tests for isValidUrl — run with: node tests/isValidUrl.test.js
"use strict";
const assert = require("assert");

// Inline the same logic as IntegrationManager.js so tests run without a browser
function isValidUrl(v) {
  if (!v || typeof v !== "string" || !v.trim()) return false;
  const s = v.trim();
  if (!/^https?:\/\//i.test(s)) return false;
  try {
    const u = new URL(s);
    return (u.protocol === "http:" || u.protocol === "https:") && !!u.hostname;
  } catch { return false; }
}

const valid = [
  "https://api.com",
  "http://api.com",
  "https://example.com/webhook",
  "https://example.com/api/events?source=oti",
  "http://localhost:3000/hook",
  "https://sub.domain.example.com/path",
];

const invalid = [
  "https:api.com",
  "http:api.com",
  "api.com",
  "www.api.com",
  "ftp://api.com",
  "https://",
  "http://",
  "",
  "   ",
  null,
  undefined,
  0,
  42,
  true,
  false,
  {},
  [],
  "//api.com",
  "https:/api.com",
];

let passed = 0;
let failed = 0;

valid.forEach(url => {
  const result = isValidUrl(url);
  if (result === true) {
    console.log(`  ✓ VALID   "${url}"`);
    passed++;
  } else {
    console.error(`  ✗ FAIL    "${url}" — expected true, got false`);
    failed++;
  }
});

invalid.forEach(url => {
  const result = isValidUrl(url);
  if (result === false) {
    console.log(`  ✓ INVALID "${url}"`);
    passed++;
  } else {
    console.error(`  ✗ FAIL    "${url}" — expected false, got true`);
    failed++;
  }
});

console.log(`\n${passed + failed} tests: ${passed} passed, ${failed} failed`);
if (failed > 0) process.exit(1);
