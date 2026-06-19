import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

#add list of page data here so all pages can use
all_pages = [
        ("Home", "/"),
        ("Hobbies", "/hobbies"),
    ]

work_experience = [
    {
        "company": "Meta x Major League Hacking",
        "location": "Remote",
        "role": "Production Engineering Fellow",
        "date": "Jun 2026 - Sep 2026",
        "description": [
            "Building production systems and open-source infrastructure at Meta scale"
        ]
    },
{
        "company": "Saddleback College Robotics",
        "location": "Mission Viejo, CA",
        "role": "Embedded Software Intern",
        "date": "May 2026 - Present",
        "description": [
            "Developing embedded firmware in C++ on Teensy microcontrollers using the Zephyr RTOS for an environmental sensing module attached to a competition Mars rover",
            "Working within ROS 2 and NAV2 framework to support autonomous navigation and mission control software for the University Rover Challenge"
        ]
    },
    {
        "company": "UCI Mass Spectrometry Facility (LUCID Platform)",
        "location": "Irvine, CA",
        "role": "Full Stack Software Engineer",
        "date": "Feb 2026 - Present",
        "description": [
            "Built and deployed a full-stack scientific search platform using React, FastAPI, AWS EC2, Route 53, and Nginx, serving 10+ researchers with sub-100ms query latency",
            "Engineered novel pattern-analysis algorithms for unidentified spectral data, enabling automated classification beyond all four reference databases and contributing to a forthcoming co-first-authored publication",
            "Diagnosed and resolved a silent-failure bug in a production data pipeline caused by Python variable scoping, restoring functionality after weeks of failed execution",
            "Developed offline desktop deployment infrastructure using PyInstaller and PyQt5 for execution across 3+ air-gapped laboratory systems"
        ]
    },
    {
        "company": "Boundary Remote Sensing Systems",
        "location": "Remote",
        "role": "Software Engineer (Data Systems)",
        "date": "Dec 2024 - Dec 2025",
        "description": [
            "Architected memory-efficient data pipelines for large-scale geophysical datasets, improving throughput while reducing memory consumption by 30%",
            "Integrated USGS and EarthScope SPUD APIs into distributed geospatial workflows, engineering fault tolerance for service failures and inconsistent data formats",
            "Implemented modular transformation and feature-extraction stages for large-scale time-series and spatial data analysis"
        ]
    },
    {
        "company": "UC Irvine Donald Bren School of ICS",
        "location": "Irvine, CA",
        "role": "ICS Learning Assistant",
        "date": "Jan 2025 - Dec 2025",
        "description": [
            "Supported 250+ students across Data Structures & Algorithms and intro C/C++ courses, covering memory management, pointer arithmetic, heap/stack behavior, and low-level data structure implementation",
            "Reinforced systems programming fundamentals through office hours and debugging support, including manual memory allocation, object lifecycle, and performance-conscious coding in C++"
        ]
    }
]

education_section = [
    {
        "school": "University of California, Irvine",
        "location": "Irvine, CA",
        "degree": "B.S. Software Engineering, Minor in Informatics",
        "date": "Expected June 2027",
        "coursework": "Computer Architecture & Organization, Operating Systems, Computer Networks, Data Structures & Algorithms, Design & Analysis of Algorithms, Database Management Systems, Information Retrieval, Discrete Mathematics, Linear Algebra, Probability & Statistics"
    }
]


all_hobbies = [
    {
        "name": "F1 Racing",
        "description": "I've been a Formula 1 fan for years, but I don't really have any pictures to share. But here is an image of a GT3RS that my friend let me drive around!",
        "image": "gt3rs.png"
    },
    {
        "name": "Hiking",
        "description": "I enjoy getting outside and exploring trails when I can. Recently did a hike in the Bay Area with some great views.",
        "image": "hike-bay-area.jpg"
    },
    {
        "name": "Specialty Matcha",
        "description": "I'm really into specialty matcha and coffee. Always on the lookout for a good matcha spot.",
        "images": ["matcha-1.png", "matcha-2.png", "matcha-3.png"]
    },
]
#pass it as an arg for rendering
@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), nav_links=all_pages, work_experience = work_experience, education_section = education_section )
@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", nav_links=all_pages, all_hobbies = all_hobbies)