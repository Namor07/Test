import streamlit as st

# --------------------------------------------------
# Seiteneinstellungen
# --------------------------------------------------
st.set_page_config(
    page_title="Tic Tac Toe",
    page_icon="❌⭕",
    layout="centered"
)

st.title("❌⭕ Tic Tac Toe")

# --------------------------------------------------
# Initialisierung des Spielzustands
# --------------------------------------------------
if "board" not in st.session_state:
    st.session_state.board = [""] * 9   # 3x3 Spielfeld
    st.session_state.current_player = "X"
    st.session_state.winner = None

# --------------------------------------------------
# Funktion: Gewinner prüfen
# --------------------------------------------------
def check_winner(board):
    """Überprüft, ob ein Spieler gewonnen hat oder Unentschieden ist"""
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Reihen
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Spalten
        (0, 4, 8), (2, 4, 6)              # Diagonalen
    ]

    for a, b, c in win_combinations:
        if board[a] == board[b] == board[c] != "":
            return board[a]

    if "" not in board:
        return "Unentschieden"

    return None

# --------------------------------------------------
# Funktion: Spielzug ausführen
# --------------------------------------------------
def make_move(index):
    """Setzt das Symbol des aktuellen Spielers"""
    if st.session_state.board[index] == "" and st.session_state.winner is None:
        st.session_state.board[index] = st.session_state.current_player
        st.session_state.winner = check_winner(st.session_state.board)

        # Spieler wechseln
        if st.session_state.winner is None:
            st.session_state.current_player = (
                "O" if st.session_state.current_player == "X" else "X"
            )

# --------------------------------------------------
# Spielfeld anzeigen (3x3 Grid)
# --------------------------------------------------
cols = st.columns(3)

for i in range(9):
    with cols[i % 3]:
        st.button(
            st.session_state.board[i] if st.session_state.board[i] else " ",
            key=i,
            on_click=make_move,
            args=(i,),
            use_container_width=True
        )

# --------------------------------------------------
# Spielstatus anzeigen
# --------------------------------------------------
st.divider()

if st.session_state.winner:
    if st.session_state.winner == "Unentschieden":
        st.success("🤝 Das Spiel endet unentschieden!")
    else:
        st.success(f"🎉 Spieler **{st.session_state.winner}** hat gewonnen!")
else:
    st.info(f"👉 Spieler **{st.session_state.current_player}** ist am Zug")

# --------------------------------------------------
# Spiel zurücksetzen
# --------------------------------------------------
if st.button("🔄 Spiel neu starten"):
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None
