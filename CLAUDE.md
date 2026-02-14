# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a static portfolio website generator that uses Python with Jinja2 templating. It reads portfolio data from a JSON file and renders HTML output for both a main portfolio page and a print-friendly resume.

## Commands

**Generate the portfolio site:**
```bash
python generate_portfolio.py
```

This reads `portfolio.json` and outputs three HTML files:
- `index.html` - Main portfolio page with featured projects
- `projects.html` - Detailed projects page with all projects, academic work, certifications, and achievements
- `resume.html` - Print-friendly resume

**Install dependencies (using uv):**
```bash
uv sync
```

Dependencies: Jinja2 (templating), Markdown (markdown to HTML conversion), Pygments (code syntax highlighting)

## Architecture

**Data Flow:** `portfolio.json` → `generate_portfolio.py` → `index.html` / `projects.html` / `resume.html`

**Key Files:**
- `portfolio.json` - All portfolio content (personal info, work experience, projects, academic projects, certifications, achievements, education, skills, interests, hobbies, languages)
- `index_template.html` - Jinja2 template for the main portfolio page with featured projects
- `projects_template.html` - Jinja2 template for detailed projects page with three sections (professional, academic, certifications/achievements)
- `resume_template.html` - Jinja2 template for a simplified, print-optimized resume
- `generate_portfolio.py` - Template rendering script with markdown processing and SVG inlining

**Markdown Support:**
- Projects can include `detailed_description` field with markdown content
- Markdown is processed using Python-Markdown library with extensions (tables, code highlighting, etc.)
- Jinja2 custom filter `markdown` converts markdown to HTML during generation

**Content Structure in portfolio.json:**

*Social Links:*
- `social_links[].svg_path` - References SVG files in `img/` that get inlined during generation

*Professional Projects:*
- `projects[].featured` - Boolean flag for displaying on main portfolio (true = featured)
- `projects[].slug` - URL-friendly identifier for anchor links (e.g., "project-name")
- `projects[].detailed_description` - Markdown content for detailed project page
- `projects[].tech_stack[]` - Array of technology names displayed as badges
- `projects[].project_date` - Project completion date in YYYY-MM format
- `projects[].repository_url` - GitHub or code repository link (optional)
- `projects[].demo_url` - Live demo URL (optional)
- `projects[].images[].img_path` - References images in `portfolio_media/`

*Academic Projects:*
- `academic_projects[]` - Array of undergraduate/academic projects
- Same structure as professional projects (slug, detailed_description, tech_stack, highlights, etc.)

*Certifications:*
- `certifications[].title` - Certification name
- `certifications[].issuer` - Certifying organization
- `certifications[].date` - Date earned in YYYY-MM format
- `certifications[].description` - Details (score, specialization, etc.)
- `certifications[].credential_url` - Link to credential (optional)

*Achievements:*
- `achievements[].title` - Achievement title
- `achievements[].description` - Details about the achievement
- `achievements[].date` - Date in YYYY-MM format
- `achievements[].category` - Category (Academic, Leadership, Sports, etc.)

**Stylesheets:**
- `css/main.css` - Primary styles for portfolio, projects page, markdown content, and components
- `css/resume.css` - Additional styles for the resume page only

**Pages:**
- `index.html` - Main portfolio featuring selected projects only (those with `featured: true`)
- `projects.html` - Complete projects showcase with three sections:
  1. Professional Projects (all projects with detailed markdown)
  2. Academic Projects (undergraduate work with detailed markdown)
  3. Certifications & Achievements (categorized lists)
- `resume.html` - Print-friendly resume
