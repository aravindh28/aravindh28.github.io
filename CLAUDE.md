# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a static portfolio website generator that uses Python with Jinja2 templating. It reads portfolio data from a JSON file and renders HTML output for both a main portfolio page and a print-friendly resume.

## Commands

**Generate the portfolio site:**
```bash
python generate_portfolio.py
```

This reads `portfolio.json` and outputs `index.html` (portfolio) and `resume.html` (resume).

**Install dependencies (using uv):**
```bash
uv sync
```

Jinja2 is required and should be installed in the virtual environment.

## Architecture

**Data Flow:** `portfolio.json` → `generate_portfolio.py` → `index.html` / `resume.html`

**Key Files:**
- `portfolio.json` - All portfolio content (personal info, work experience, projects, education, skills, interests, hobbies, languages)
- `index_template.html` - Jinja2 template for the main portfolio page with sidebar layout
- `resume_template.html` - Jinja2 template for a simplified, print-optimized resume
- `generate_portfolio.py` - Template rendering script that also injects SVG icons from `img/` for social links

**Content Structure in portfolio.json:**
- `social_links[].svg_path` - References SVG files in `img/` that get inlined during generation
- `work_experience[].company_favicon` - References images in `portfolio_media/`
- `projects[].images[].img_path` - References images in `portfolio_media/`

**Stylesheets:**
- `css/main.css` - Primary styles for the portfolio
- `css/resume.css` - Additional styles for the resume page only
