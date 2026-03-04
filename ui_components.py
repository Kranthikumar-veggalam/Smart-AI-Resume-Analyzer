import streamlit as st

def apply_modern_styles():
    """Apply modern styles by loading the CSS file"""
    # Styles are now loaded from style.css in app.py
    pass

def page_header(title, subtitle=None):
    """Render a consistent page header with gradient background"""
    st.markdown(
        f'''
        <div class="page-header" style="background: transparent; border: none;">
            <h1 class="header-title glow-text" style="font-size: 3rem; margin-bottom: 0.5rem;">{title}</h1>
            {f'<p class="header-subtitle" style="color: var(--text-secondary); font-size: 1.2rem;">{subtitle}</p>' if subtitle else ''}
        </div>
        ''',
        unsafe_allow_html=True
    )

def hero_section(title, subtitle=None, description=None):
    """Render a modern hero section with gradient background and animations"""
    # If description is provided but subtitle is not, use description as subtitle
    if description and not subtitle:
        subtitle = description
        description = None
    
    st.markdown(
        f'''
        <div class="page-header hero-header" style="background: transparent; border: none; padding-top: 2rem;">
            <h1 class="header-title animated-gradient-text" style="font-size: 4rem; margin-bottom: 1rem;">{title}</h1>
            {f'<div class="header-subtitle" style="color: var(--text-primary); font-size: 1.5rem; font-weight: 500;">{subtitle}</div>' if subtitle else ''}
            {f'<p class="header-description" style="color: var(--text-secondary); margin-top: 1rem; max-width: 800px; margin-left: auto; margin-right: auto;">{description}</p>' if description else ''}
        </div>
        ''',
        unsafe_allow_html=True
    )

def feature_card(icon, title, description):
    """Render a modern feature card with hover effects"""
    st.markdown(f"""
        <div class="glass-card feature-card" style="padding: 2rem; text-align: center; height: 100%;">
            <div class="feature-icon icon-pulse" style="font-size: 3rem; margin-bottom: 1rem;">
                <i class="{icon}"></i>
            </div>
            <h3 style="color: var(--accent-secondary); font-size: 1.5rem; margin-bottom: 1rem;">{title}</h3>
            <p style="color: var(--text-secondary); font-size: 1.05rem; line-height: 1.6;">{description}</p>
        </div>
    """, unsafe_allow_html=True)

def about_section(content, image_path=None, social_links=None):
    """Render a modern about section with profile image and social links"""
    st.markdown("""
        <div class="glass-card about-section" style="padding: 3rem;">
            <div class="profile-section" style="display: flex; flex-direction: column; align-items: center; gap: 2rem;">
    """, unsafe_allow_html=True)
    
    # Profile Image
    if image_path:
        st.image(image_path, use_column_width=False, width=200)
    
    # Image Upload
    uploaded_file = st.file_uploader("Upload profile picture", type=['png', 'jpg', 'jpeg'])
    if uploaded_file is not None:
        st.image(uploaded_file, use_column_width=False, width=200)
    
    # Social Links
    if social_links:
        st.markdown('<div class="social-links" style="display: flex; gap: 1.5rem; justify-content: center;">', unsafe_allow_html=True)
        for platform, url in social_links.items():
            st.markdown(f'<a href="{url}" target="_blank" class="social-link" style="font-size: 2rem; color: var(--accent-secondary); transition: all 0.3s ease;"><i class="fab fa-{platform.lower()}"></i></a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # About Content
    st.markdown(f"""
            </div>
            <div class="about-content" style="margin-top: 2rem; font-size: 1.1rem; color: var(--text-secondary); line-height: 1.8; text-align: center; max-width: 800px; margin-left: auto; margin-right: auto;">{content}</div>
        </div>
    """, unsafe_allow_html=True)

def metric_card(label, value, delta=None, icon=None):
    """Render a modern metric card with animations"""
    icon_html = f'<i class="{icon}" style="color: var(--accent-primary); font-size: 1.5rem;"></i>' if icon else ''
    delta_html = f'<div class="metric-delta" style="color: var(--success); font-size: 0.9rem; margin-top: 0.5rem; font-weight: 600;">{delta}</div>' if delta else ''
    
    st.markdown(f"""
        <div class="glass-card metric-card" style="padding: 1.5rem; display: flex; flex-direction: column; gap: 0.5rem;">
            <div class="metric-header" style="display: flex; align-items: center; gap: 0.8rem; margin-bottom: 0.5rem;">
                {icon_html}
                <div class="metric-label" style="color: var(--text-secondary); text-transform: uppercase; font-size: 0.85rem; letter-spacing: 1px;">{label}</div>
            </div>
            <div class="metric-value glow-text" style="font-size: 2.5rem; font-weight: 800; font-family: 'Space Grotesk', sans-serif; line-height: 1;">{value}</div>
            {delta_html}
        </div>
    """, unsafe_allow_html=True)

def template_card(title, description, image_url=None):
    """Render a modern template card with glassmorphism effect"""
    image_html = f'<img src="{image_url}" class="template-image" style="width: 100%; border-radius: 8px; margin-bottom: 1rem;" />' if image_url else ''
    
    st.markdown(f"""
        <div class="glass-card template-card" style="padding: 1.5rem; display: flex; flex-direction: column; height: 100%;">
            {image_html}
            <h3 style="color: var(--accent-secondary); font-size: 1.2rem; margin-bottom: 0.5rem;">{title}</h3>
            <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.5;">{description}</p>
        </div>
    """, unsafe_allow_html=True)

def feedback_card(name, feedback, rating):
    """Render a modern feedback card with rating stars"""
    stars = "⭐" * int(rating)
    
    st.markdown(f"""
        <div class="glass-card feedback-card" style="padding: 1.5rem; margin-bottom: 1rem;">
            <div class="feedback-header" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                <div class="feedback-name" style="font-weight: 600; color: var(--accent-secondary); font-size: 1.1rem;">{name}</div>
                <div class="feedback-rating" style="letter-spacing: 2px;">{stars}</div>
            </div>
            <p class="feedback-text" style="color: var(--text-secondary); font-size: 1rem; line-height: 1.6; font-style: italic;">"{feedback}"</p>
        </div>
    """, unsafe_allow_html=True)

def loading_spinner(message="Loading..."):
    """Show a modern loading spinner with message"""
    st.markdown(f"""
        <div class="loading-container">
            <div class="loading-spinner"></div>
            <p class="loading-message">{message}</p>
        </div>
    """, unsafe_allow_html=True)

def progress_bar(value, max_value, label=None):
    """Render a modern animated progress bar"""
    percentage = min(100, max(0, (value / max_value) * 100))
    label_html = f'<div class="progress-label" style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;"><span style="color: var(--text-secondary); font-weight: 500;">{label}</span><span style="color: var(--accent-secondary); font-weight: 600;">{percentage:.1f}%</span></div>' if label else ''
    
    st.markdown(f"""
        <div class="progress-wrap" style="margin-bottom: 1.5rem;">
            {label_html}
            <div class="progress-container" style="background: rgba(255,255,255,0.05); border-radius: 50px; height: 10px; overflow: hidden; border: 1px solid var(--border-glass);">
                <div class="progress-fill" style="width: {percentage}%; background: var(--gradient-primary); height: 100%; border-radius: 50px; box-shadow: 0 0 10px rgba(124, 58, 236, 0.5); transition: width 1s ease-in-out;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def tooltip(content, tooltip_text):
    """Render content with a modern tooltip"""
    st.markdown(f"""
        <div class="tooltip" data-tooltip="{tooltip_text}">
            {content}
        </div>
    """, unsafe_allow_html=True)

def data_table(data, headers):
    """Render a modern data table with hover effects"""
    header_row = "".join([f"<th>{header}</th>" for header in headers])
    rows = ""
    for row in data:
        cells = "".join([f"<td>{cell}</td>" for cell in row])
        rows += f"<tr>{cells}</tr>"
    
    st.markdown(f"""
        <div class="table-container">
            <table class="modern-table">
                <thead>
                    <tr>{header_row}</tr>
                </thead>
                <tbody>
                    {rows}
                </tbody>
            </table>
        </div>
    """, unsafe_allow_html=True)

def grid_layout(*elements):
    """Create a responsive grid layout"""
    st.markdown("""
        <div class="grid">
            {}
        </div>
    """.format("".join(elements)), unsafe_allow_html=True)

def alert(message, type="info"):
    """Display a modern alert message"""
    st.markdown(f"""
        <div class="alert alert-{type}" style="display: flex; gap: 1rem; padding: 1rem 1.5rem; border-radius: 8px; margin-bottom: 1rem; align-items: center;">
            <span class="alert-message" style="font-weight: 500; letter-spacing: 0.3px;">{message}</span>
        </div>
    """, unsafe_allow_html=True)

    # Removed unused complex about_section inline styling

def generate_team_section(team_members):
    if not team_members:
        return ""
    
    team_html = ['<div class="team-section">']
    for member in team_members:
        team_html.append(f"""
            <div class="team-member">
                <img src="{member['image']}" alt="{member['name']}">
                <h3>{member['name']}</h3>
                <p>{member['role']}</p>
            </div>
        """)
    team_html.append('</div>')
    return "".join(team_html)

def render_feedback(feedback_data):
    """Render feedback with modern styling"""
    if not feedback_data:
        return
    
    feedback_html = ["""
    <div class="feedback-section">
        <h3 class="feedback-header">Resume Analysis Feedback</h3>
        <div class="feedback-content">
    """]
    
    for category, items in feedback_data.items():
        if items:  # Only show categories with feedback
            for item in items:
                feedback_html.append(f"""
                <div class="feedback-item">
                    <div class="feedback-category">{category}</div>
                    <div class="feedback-description">{item}</div>
                </div>
                """)
    
    feedback_html.append("""
        </div>
    </div>
    """)
    
    st.markdown("".join(feedback_html), unsafe_allow_html=True)

def render_analytics_section(resume_uploaded=False, metrics=None):
    """Render the analytics section of the dashboard"""
    if not metrics:
        metrics = {
            'views': 0,
            'downloads': 0,
            'score': 'N/A'
        }
    
    # Views Card
    st.markdown("""
        <div class="glass-card" style='padding: 2rem; text-align: center; margin-bottom: 1rem;'>
            <div style='color: var(--accent-secondary); font-size: 2.5rem; margin-bottom: 1rem;'>
                <i class='fas fa-eye icon-pulse'></i>
            </div>
            <h2 style='color: var(--text-primary); font-size: 1.3rem; margin-bottom: 0.5rem;'>Resume Views</h2>
            <p class="glow-text" style='font-size: 2.5rem; font-weight: bold; margin: 0;'>{}</p>
        </div>
    """.format(metrics['views']), unsafe_allow_html=True)
    
    # Downloads Card
    st.markdown("""
        <div class="glass-card" style='padding: 2rem; text-align: center; margin-bottom: 1rem;'>
            <div style='color: var(--accent-primary); font-size: 2.5rem; margin-bottom: 1rem;'>
                <i class='fas fa-download icon-pulse'></i>
            </div>
            <h2 style='color: var(--text-primary); font-size: 1.3rem; margin-bottom: 0.5rem;'>Downloads</h2>
            <p class="glow-text" style='font-size: 2.5rem; font-weight: bold; margin: 0;'>{}</p>
        </div>
    """.format(metrics['downloads']), unsafe_allow_html=True)
    
    # Profile Score Card
    st.markdown("""
        <div class="glass-card" style='padding: 2rem; text-align: center; margin-bottom: 1rem;'>
            <div style='color: var(--success); font-size: 2.5rem; margin-bottom: 1rem;'>
                <i class='fas fa-chart-line icon-pulse'></i>
            </div>
            <h2 style='color: var(--text-primary); font-size: 1.3rem; margin-bottom: 0.5rem;'>Profile Score</h2>
            <p class="glow-text" style='font-size: 2.5rem; font-weight: bold; margin: 0;'>{}</p>
        </div>
    """.format(metrics['score']), unsafe_allow_html=True)

def render_activity_section(resume_uploaded=False):
    """Render the recent activity section"""
    st.markdown("""
        <div class="glass-card" style='padding: 2rem; height: 100%; border-left: 3px solid var(--accent-secondary);'>
            <h2 style='color: var(--text-primary); font-size: 1.5rem; margin-bottom: 1.5rem; display: flex; align-items: center;'>
                <i class='fas fa-history' style='color: var(--accent-secondary); margin-right: 0.8rem; font-size: 1.2rem;'></i> Recent Activity
            </h2>
    """, unsafe_allow_html=True)
    
    if resume_uploaded:
        st.markdown("""
            <div style='color: var(--text-secondary);'>
                <p style='margin: 1rem 0; font-size: 1.05rem; display: flex; align-items: center;'><i class="fas fa-check-circle" style="color: var(--success); margin-right: 0.8rem;"></i> Resume uploaded and analyzed</p>
                <div style="height: 1px; background: var(--border-glass); margin: 0.5rem 0;"></div>
                <p style='margin: 1rem 0; font-size: 1.05rem; display: flex; align-items: center;'><i class="fas fa-check-circle" style="color: var(--success); margin-right: 0.8rem;"></i> Generated optimization suggestions</p>
                <div style="height: 1px; background: var(--border-glass); margin: 0.5rem 0;"></div>
                <p style='margin: 1rem 0; font-size: 1.05rem; display: flex; align-items: center;'><i class="fas fa-check-circle" style="color: var(--success); margin-right: 0.8rem;"></i> Updated profile score</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style='text-align: center; padding: 3rem 1rem; color: var(--text-muted);'>
                <i class='fas fa-upload icon-pulse' style='font-size: 3rem; color: var(--border-glass-highlight); margin-bottom: 1.5rem;'></i>
                <p style='margin: 0; font-size: 1.1rem;'>Upload your resume to see activity</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

def render_suggestions_section(resume_uploaded=False):
    """Render the suggestions section"""
    st.markdown("""
        <div class="glass-card" style='padding: 2rem; height: 100%; border-left: 3px solid var(--accent-primary);'>
            <h2 style='color: var(--text-primary); font-size: 1.5rem; margin-bottom: 1.5rem; display: flex; align-items: center;'>
                <i class='fas fa-lightbulb' style='color: var(--accent-primary); margin-right: 0.8rem; font-size: 1.2rem;'></i> Suggestions
            </h2>
    """, unsafe_allow_html=True)
    
    if resume_uploaded:
        st.markdown("""
            <div style='color: var(--text-secondary);'>
                <p style='margin: 1rem 0; font-size: 1.05rem; display: flex; align-items: start;'><i class="fas fa-arrow-right" style="color: var(--accent-primary); margin-right: 0.8rem; margin-top: 0.3rem;"></i> Add more quantifiable achievements</p>
                <div style="height: 1px; background: var(--border-glass); margin: 0.5rem 0;"></div>
                <p style='margin: 1rem 0; font-size: 1.05rem; display: flex; align-items: start;'><i class="fas fa-arrow-right" style="color: var(--accent-primary); margin-right: 0.8rem; margin-top: 0.3rem;"></i> Include relevant keywords based on target job description</p>
                <div style="height: 1px; background: var(--border-glass); margin: 0.5rem 0;"></div>
                <p style='margin: 1rem 0; font-size: 1.05rem; display: flex; align-items: start;'><i class="fas fa-arrow-right" style="color: var(--accent-primary); margin-right: 0.8rem; margin-top: 0.3rem;"></i> Optimize formatting for better ATS parsing</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style='text-align: center; padding: 3rem 1rem; color: var(--text-muted);'>
                <i class='fas fa-file-alt icon-pulse' style='font-size: 3rem; color: var(--border-glass-highlight); margin-bottom: 1.5rem;'></i>
                <p style='margin: 0; font-size: 1.1rem;'>Upload your resume to get AI-powered suggestions</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)