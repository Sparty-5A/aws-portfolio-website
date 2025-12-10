#!/bin/bash
# Add Pulumi vs Terraform explanation to portfolio

echo "🔧 Adding Pulumi explanation to your portfolio..."
echo ""

# Check if we're in the right directory
if [ ! -f "website/about.html" ]; then
    echo "❌ Error: website/about.html not found!"
    echo "Please run this script from the pulumi-s3-cloudfront directory"
    exit 1
fi

# Backup original files
echo "📦 Creating backups..."
cp website/about.html website/about.html.backup
cp website/css/style.css website/css/style.css.backup

# Download the snippet
echo "📥 Adding Pulumi explanation section..."

# The HTML content to add (simplified for insertion)
cat >> website/about.html << 'HTMLEOF'

            <!-- Infrastructure as Code Philosophy -->
            <div class="about-section">
                <h2>Infrastructure as Code Approach</h2>
                
                <div class="iac-explanation">
                    <h3>Why Pulumi Over Terraform?</h3>
                    <p>
                        All projects in this portfolio use <strong>Pulumi</strong> for Infrastructure 
                        as Code instead of the more commonly known Terraform. This choice demonstrates 
                        several key advantages:
                    </p>
                    
                    <div class="comparison-grid">
                        <div class="comparison-card">
                            <h4>🐍 Native Programming Languages</h4>
                            <p>
                                Pulumi uses <strong>Python</strong> instead of HashiCorp Configuration 
                                Language (HCL). This means using familiar programming constructs like 
                                loops, conditionals, and functions rather than learning a domain-specific 
                                language.
                            </p>
                        </div>

                        <div class="comparison-card">
                            <h4>⚡ Type Safety & IDE Support</h4>
                            <p>
                                Full IDE autocomplete, type checking, and inline documentation. Errors 
                                are caught at development time, not deployment time, dramatically speeding 
                                up development.
                            </p>
                        </div>

                        <div class="comparison-card">
                            <h4>🔧 Programming Flexibility</h4>
                            <p>
                                Complex logic that requires dozens of lines in HCL can be expressed 
                                simply using Python's standard library. Need to parse JSON or perform 
                                calculations? Just use Python.
                            </p>
                        </div>

                        <div class="comparison-card">
                            <h4>📦 Reusable Components</h4>
                            <p>
                                Create reusable infrastructure components as Python classes or functions, 
                                enabling infrastructure libraries that can be shared across projects.
                            </p>
                        </div>

                        <div class="comparison-card">
                            <h4>🧪 Testing & Validation</h4>
                            <p>
                                Infrastructure can be unit tested using standard Python testing frameworks 
                                (pytest, unittest). Test your infrastructure logic before deploying.
                            </p>
                        </div>

                        <div class="comparison-card">
                            <h4>🤝 Terraform Compatibility</h4>
                            <p>
                                Pulumi can import existing Terraform state and use Terraform providers. 
                                Teams can migrate gradually.
                            </p>
                        </div>
                    </div>

                    <div class="iac-comparison-table">
                        <h4>Quick Comparison</h4>
                        <table>
                            <thead>
                                <tr>
                                    <th>Feature</th>
                                    <th>Pulumi</th>
                                    <th>Terraform</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Language</td>
                                    <td>Python, TypeScript, Go, C#</td>
                                    <td>HCL (proprietary)</td>
                                </tr>
                                <tr>
                                    <td>Type Safety</td>
                                    <td>✅ Full (compile-time)</td>
                                    <td>⚠️ Limited</td>
                                </tr>
                                <tr>
                                    <td>IDE Support</td>
                                    <td>✅ Full autocomplete</td>
                                    <td>⚠️ Basic</td>
                                </tr>
                                <tr>
                                    <td>Testing</td>
                                    <td>✅ Unit & integration tests</td>
                                    <td>⚠️ Limited</td>
                                </tr>
                                <tr>
                                    <td>Loops & Logic</td>
                                    <td>✅ Native programming</td>
                                    <td>⚠️ count/for_each only</td>
                                </tr>
                                <tr>
                                    <td>Community</td>
                                    <td>⚠️ Growing</td>
                                    <td>✅ Very large</td>
                                </tr>
                                <tr>
                                    <td>Maturity</td>
                                    <td>⚠️ Newer (2017)</td>
                                    <td>✅ Mature (2014)</td>
                                </tr>
                                <tr>
                                    <td>State Backend</td>
                                    <td>✅ Free cloud backend</td>
                                    <td>💰 Paid (Terraform Cloud)</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <div class="iac-note">
                        <p>
                            <strong>Note:</strong> Both Pulumi and Terraform are excellent IaC tools. 
                            Terraform has a larger community and more mature ecosystem. However, for 
                            developers comfortable with general-purpose programming languages, Pulumi 
                            offers a more intuitive development experience.
                        </p>
                        <p>
                            In professional settings, I'm prepared to work with either tool based on 
                            team preferences and existing infrastructure.
                        </p>
                    </div>
                </div>
            </div>
HTMLEOF

# Add CSS
echo "🎨 Adding CSS styles..."
cat >> website/css/style.css << 'CSSEOF'

/* Infrastructure as Code Section */
.iac-explanation{background:var(--card-bg);padding:var(--spacing-xl);border-radius:12px;border:1px solid var(--border-color)}.iac-explanation h3{color:var(--accent-primary);margin-bottom:var(--spacing-md)}.iac-explanation>p{color:var(--text-secondary);font-size:1.1rem;margin-bottom:var(--spacing-xl)}.comparison-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:var(--spacing-lg);margin-bottom:var(--spacing-xl)}.comparison-card{background:var(--bg-tertiary);padding:var(--spacing-lg);border-radius:8px;border-left:4px solid var(--accent-primary)}.comparison-card h4{margin-bottom:var(--spacing-sm);font-size:1.1rem}.comparison-card p{color:var(--text-muted);font-size:.95rem;line-height:1.6}.iac-comparison-table{margin:var(--spacing-xl) 0}.iac-comparison-table h4{margin-bottom:var(--spacing-md);color:var(--accent-primary)}.iac-comparison-table table{width:100%;border-collapse:collapse;background:var(--bg-tertiary);border-radius:8px;overflow:hidden}.iac-comparison-table td,.iac-comparison-table th{padding:var(--spacing-sm);text-align:left;border-bottom:1px solid var(--border-color)}.iac-comparison-table th{background:var(--bg-primary);color:var(--accent-primary);font-weight:600}.iac-comparison-table td{color:var(--text-secondary)}.iac-comparison-table tr:last-child td{border-bottom:none}.iac-note{background:var(--bg-secondary);padding:var(--spacing-lg);border-radius:8px;border:1px solid var(--border-color);margin-top:var(--spacing-xl)}.iac-note p{color:var(--text-muted);margin-bottom:var(--spacing-sm)}.iac-note p:last-child{margin-bottom:0}.iac-note strong{color:var(--accent-primary)}@media (max-width:768px){.comparison-grid{grid-template-columns:1fr}.iac-comparison-table{overflow-x:auto}.iac-comparison-table table{min-width:600px}}
CSSEOF

echo ""
echo "✅ Successfully added Pulumi explanation!"
echo ""
echo "📝 Changes made:"
echo "   • Added 'Infrastructure as Code Approach' section to about.html"
echo "   • Added CSS styling for the new section"
echo ""
echo "💾 Backups created:"
echo "   • website/about.html.backup"
echo "   • website/css/style.css.backup"
echo ""
echo "🔄 Next steps:"
echo "   1. Open website/about.html in your browser to preview"
echo "   2. If you like it: pulumi up"
echo "   3. If you don't: restore from backups"
echo ""
echo "🎉 Done!"
