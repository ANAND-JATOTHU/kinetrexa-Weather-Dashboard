import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generate_pdf_report(filename="Project_Report.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    
    # Title
    title_style = styles['Title']
    story.append(Paragraph("Weather Dashboard - Project Report", title_style))
    story.append(Spacer(1, 20))
    
    # Project Overview
    h2_style = styles['Heading2']
    story.append(Paragraph("Project Overview", h2_style))
    overview_text = """
    The Weather Dashboard is a full-stack Python Django application. It allows users to register, log in, 
    and manage a personalized dashboard of favorite cities. The application fetches real-time weather data 
    and a 5-day forecast using the OpenWeatherMap API.
    """
    story.append(Paragraph(overview_text, styles['Normal']))
    story.append(Spacer(1, 15))
    
    # System Architecture
    story.append(Paragraph("System Architecture", h2_style))
    arch_text = """
    The architecture follows the MVT (Model-View-Template) pattern:
    - <b>Models:</b> Define the database schema (User, FavoriteLocation, WeatherSearchLog).
    - <b>Views:</b> Handle business logic, utilizing Class-Based Views (CBVs) for CRUD operations.
    - <b>Templates:</b> Render the UI using HTML and Vanilla CSS with a glassmorphism aesthetic.
    - <b>Service Layer:</b> Encapsulates third-party API integration (OpenWeatherMap) to handle 
      data fetching, error handling (404, 429, timeouts), and parsing.
    """
    story.append(Paragraph(arch_text, styles['Normal']))
    story.append(Spacer(1, 15))
    
    # Database Schema
    story.append(Paragraph("Database Schema", h2_style))
    
    data = [
        ['Model', 'Fields', 'Relationships / Notes'],
        ['User', 'username, password, email', 'Django built-in auth model'],
        ['FavoriteLocation', 'id, user_id, city_name, custom_nickname, created_at', 'Foreign Key to User. Unique together (user, city)'],
        ['WeatherSearchLog', 'id, user_id, query_string, timestamp, status_code', 'Foreign Key to User. Used for tracking API usage and errors']
    ]
    
    t = Table(data, colWidths=[100, 150, 250])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
        ('BACKGROUND', (0,1), (-1,-1), colors.beige),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
    ]))
    story.append(t)
    story.append(Spacer(1, 20))
    
    # Error Handling & Validation
    story.append(Paragraph("Error Handling & Validation", h2_style))
    error_text = """
    - Input Sanitization: User input is cleaned via Django Forms before interacting with the database or API.
    - Graceful degradation: If the API returns a 404 (City Not Found) or 429 (Rate Limit Exceeded), the service layer 
      raises custom exceptions which are caught by the views and displayed as Django Messages to the user.
    - Network Timeouts: The requests library is configured with a 5-second timeout to prevent blocking.
    """
    story.append(Paragraph(error_text, styles['Normal']))
    
    # Build PDF
    doc.build(story)
    print(f"Report generated successfully: {filename}")

if __name__ == "__main__":
    generate_pdf_report()
