import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text

# Custom HTML for title
custom_title_html = """
<style>
.custom-title {
  font-size: 2.5rem;
  font-weight: bold;
  margin-bottom: 1rem;
}
</style>
<div class="custom-title">
  📧 Cold Email Generator
</div>
"""


def create_streamlit_app(llm, portfolio, clean_text):
    st.set_page_config(page_title="Cold Email Generator", page_icon="📧", layout="wide")

    # Use custom HTML title instead of st.title()
    st.markdown(custom_title_html, unsafe_allow_html=True)

    st.write("Enter information about yourself and the job posting URL to generate a personalized cold email.")

    # Text area for user to write about themselves
    user_info = st.text_area(
        "About Yourself:",
        placeholder="Write a brief description about your skills, experience, and why you're interested in this job...",
        help="This information will be used to personalize your cold email.",
        height=150
    )

    url_input = st.text_input(
        "Job Posting URL:",
        placeholder="https://example.com/job-posting",
        help="Paste the full URL of the job posting here"
    )

    submit_button = st.button("Generate Email")

    if submit_button:
        if not url_input or not user_info:
            st.warning("Please enter both your information and a valid URL before submitting.")
        else:
            try:
                with st.spinner("Processing job posting and generating email..."):
                    loader = WebBaseLoader([url_input])
                    data = clean_text(loader.load()[0].page_content)
                    portfolio.load_portfolio()
                    jobs = llm.extract_jobs(data)

                    if not jobs:
                        st.warning(
                            "No job information could be extracted from this URL. Please check the URL and try again.")
                    else:
                        for i, job in enumerate(jobs, 1):
                            st.subheader(f"Generated Email {i}")
                            skills = job.get('skills', [])
                            links = portfolio.query_links(skills)
                            email = llm.write_mail(job, links, user_info)
                            st.code(email, language='markdown')
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                st.error("Please check the URL and try again.")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    create_streamlit_app(chain, portfolio, clean_text)