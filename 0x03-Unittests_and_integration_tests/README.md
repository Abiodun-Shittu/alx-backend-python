# 0x03. Unittests and Integration Tests

## Tasks
### 0. Parameterize a unit test
- In this task you will write the first unit test for utils.access_nested_map.

### 1. Parameterize a unit test
- Implement TestAccessNestedMap.test_access_nested_map_exception. Use the assertRaises context manager to test that a KeyError is raised for the following inputs (use @parameterized.expand):

### 2. Mock HTTP calls
- Define the TestGetJson(unittest.TestCase) class and implement the TestGetJson.test_get_json method to test that utils.get_json returns the expected result.

### 3. Parameterize and patch
- Implement the TestMemoize(unittest.TestCase) class with a test_memoize method.

### 4. Parameterize and patch as decorators
- In a new test_client.py file, declare the TestGithubOrgClient(unittest.TestCase) class and implement the test_org method.

### 5. Mocking a property
- Implement the test_public_repos_url method to unit-test GithubOrgClient._public_repos_url.

### 6. More patching
- Implement TestGithubOrgClient.test_public_repos to unit-test GithubOrgClient.public_repos.

### 7. Parameterize
- Implement TestGithubOrgClient.test_has_license to unit-test GithubOrgClient.has_license.

### 8. Integration test: fixtures
- Create the TestIntegrationGithubOrgClient(unittest.TestCase) class and implement the setUpClass and tearDownClass which are part of the unittest.TestCase API.

### 9. Integration tests
- Implement the test_public_repos method to test GithubOrgClient.public_repos.
