describe("Index page should exist", () => {
  it("Loads the index page", () => {
    cy.visit("http://localhost:5000");
    cy.contains("Duty");
  });
});
