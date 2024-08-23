import streamlit as st

def show_forums_page():
    st.title("Peer Learning Forums")
    st.markdown("### Ask Questions, Share Knowledge, Learn Together!")
    
    # Disqus embed code
    disqus_code = """
    <div id="disqus_thread"></div>
    <script>
    var disqus_config = function () {
        this.page.url = window.location.href;
        this.page.identifier = window.location.pathname;
    };
    (function() {
    var d = document, s = d.createElement('script');
    s.src = 'https://edustream-forum.disqus.com/embed.js';  // Replace 'edustream-forum' with your Disqus shortname
    s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
    })();
    </script>
    <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
    """
    
    st.markdown(disqus_code, unsafe_allow_html=True)

if __name__ == "__main__":
    show_forums_page()
