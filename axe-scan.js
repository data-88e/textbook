const { Builder } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');
const AxeBuilder = require('@axe-core/webdriverjs');
const fs = require('fs');

// Get URLs from command line args
const urls = process.argv.slice(2);

(async function scan() {
  const options = new chrome.Options();
  options.addArguments('--headless=new'); 
  options.addArguments('--no-sandbox');
  options.addArguments('--disable-dev-shm-usage'); 
  options.addArguments('--disable-gpu');
  
  // Initialize Driver
  const driver = await new Builder()
    .forBrowser('chrome')
    .setChromeOptions(options)
    .build();

  const fullReport = [];
  let hasErrors = false;

  try {
    // Set a very generous timeout for page loads (3 minutes)
    await driver.manage().setTimeouts({ pageLoad: 180000, script: 180000 });

    for (const url of urls) {
      console.log(`Testing ${url} ...`);
      
      try {
        await driver.get(url);

        // Run Axe analysis
        const results = await new AxeBuilder(driver)
          .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
          .analyze();

        if (results.violations.length > 0) {
          console.log(`  FAILED: ${results.violations.length} violations found.`);
          fullReport.push({
            url: url,
            violations: results.violations
          });
          hasErrors = true; 
        } else {
          console.log(`  PASSED`);
        }
        
      } catch (e) {
        console.error(`  CRASHED: Could not scan ${url}. Skipping.`);
        console.error(`  Reason: ${e.message}`);
        fullReport.push({
          url: url,
          error: "Browser crashed or timed out on this page",
          details: e.message
        });
        hasErrors = true;
      }
    }

    fs.writeFileSync('axe-report.json', JSON.stringify(fullReport, null, 2));
    console.log('Report saved to axe-report.json');

  } finally {
    await driver.quit();
  }

  if (hasErrors) {
    process.exit(1);
  }
})();