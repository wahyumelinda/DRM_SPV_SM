import streamlit as st

st.set_page_config(page_title="Login", page_icon="🔐", layout="wide")

# Dummy database (bisa diganti dengan database nyata)
USER = {
    "SPV": {"username": "supervisor", "password": "spv123"},
    "SM": {"username": "manager", "password": "sm123"}
}

# Session state
if "role" not in st.session_state:
    st.session_state.role = None
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Header berubah jika sudah login
if st.session_state.logged_in:
    header_text = f"✅ Welcome to the {st.session_state.role} Approval System"
    header_color = "#58D68D"  # Warna hijau untuk tampilan saat sudah login
else:
    header_text = "🔐 Welcome to the Approval System"
    header_color = "#5DADE2"  # Warna biru muda

st.markdown(
    f"""
    <h1 style='text-align: center; color: white; background-color: {header_color}; padding: 15px; border-radius: 10px;'>
        {header_text}
    </h1>
    """, 
    unsafe_allow_html=True
)

# Jika belum login, tampilkan pilihan role
if not st.session_state.logged_in:
    st.markdown("<h3 style='text-align: center;'>Silakan pilih role Anda untuk login:</h3>", unsafe_allow_html=True)

    if st.button("🛠 Supervisor (SPV)", use_container_width=True, help="Login sebagai Supervisor"):
        st.session_state.role = "SPV"
        st.rerun()

    if st.button("📊 Section Manager (SM)", use_container_width=True, help="Login sebagai Section Manager"):
        st.session_state.role = "SM"
        st.rerun()

# Login page hanya muncul jika role sudah dipilih dan belum login
if st.session_state.role and not st.session_state.logged_in:
    st.subheader(f"🔑 Login sebagai {st.session_state.role}")

    username = st.text_input("👤 Username")
    password = st.text_input("🔒 Password", type="password")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✅ Login", use_container_width=True):
            creds = USER.get(st.session_state.role, {})

            if username == creds.get("username") and password == creds.get("password"):
                st.session_state.logged_in = True
                st.success("✅ Login berhasil! Redirecting...")
                st.rerun()
            else:
                st.error("❌ Username atau password salah!")

# Redirect ke form sesuai role yang dipilih
if st.session_state.logged_in:
    if st.button("Klik untuk Logout 🔓", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.role = None
        st.rerun()


    if st.session_state.role == "SPV":
        import update_SPV  
        update_SPV.run()
    elif st.session_state.role == "SM":
        import update_SM
        update_SM.run()