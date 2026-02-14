# Portfolio Generator

A static portfolio website generator that uses Python with Jinja2 templating to create a professional portfolio site from JSON data.

## Project Structure

```
portfolio_generator/
├── portfolio.json           # Portfolio content (personal info, projects, experience, etc.)
├── generate_portfolio.py    # Main script to generate HTML from templates
├── index_template.html      # Template for main portfolio page (featured projects)
├── projects_template.html   # Template for detailed projects page
├── resume_template.html     # Template for print-friendly resume
├── index.html              # Generated main portfolio page
├── projects.html           # Generated projects page
├── resume.html             # Generated resume page
├── css/
│   ├── main.css            # Primary styles for portfolio and projects
│   └── resume.css          # Additional styles for resume page
├── img/                    # SVG icons and images
└── portfolio_media/        # Project images and media files
```

## Quick Start

**Install dependencies:**
```bash
uv sync
```

**Generate the portfolio site:**
```bash
python generate_portfolio.py
```

This reads `portfolio.json` and outputs three HTML files:
- `index.html` - Main portfolio page with featured projects
- `projects.html` - Detailed projects page with all projects, academic work, certifications, and achievements
- `resume.html` - Print-friendly resume

## Features

- **JSON-driven content**: All portfolio data in a single `portfolio.json` file
- **Markdown support**: Write detailed project descriptions in Markdown
- **Three-page output**: Portfolio, detailed projects, and print resume
- **SVG inlining**: Social media icons automatically inlined during generation
- **Responsive design**: Works on desktop, tablet, and mobile devices
- **Print-optimized resume**: Clean, professional resume layout for printing

## Attribution

Created by Aravindh and [Claude Code](https://claude.com/claude-code).

Based on [Corey Schafer's portfolio template](https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog).
