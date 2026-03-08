import { useState } from "react";

const API = "http://127.0.0.1:8000"; // change if needed

async function apiFetch(path, body, token) {
  const headers = { "Content-Type": "application/json" };
  if (token) headers["Authorization"] = `Bearer ${token}`;
  const res = await fetch(`${API}${path}`, {
    method: "POST",
    headers,
    body: JSON.stringify(body),
  });
  const data = await res.json();
  return { ok: res.ok, status: res.status, data };
}

export default function App() {
  // ── Auth ──
  const [email,    setEmail]    = useState("");
  const [password, setPassword] = useState("");
  const [token,    setToken]    = useState("");
  const [authResult, setAuthResult] = useState(null);
  const [authLoading, setAuthLoading] = useState(false);

  // ── Watchlist ──
  const [addId,     setAddId]     = useState("");
  const [removeId,  setRemoveId]  = useState("");
  const [watchedId, setWatchedId] = useState("");
  const [rating,    setRating]    = useState("3.5");
  const [tag,       setTag]       = useState("");

  const [results,  setResults]  = useState({});
  const [loading,  setLoading]  = useState("");

  // ── Login to get token ──
  const login = async () => {
    setAuthLoading(true);
    const res = await apiFetch("/auth/login", { email, password });
    setAuthResult(res);
    if (res.ok && res.data.access_token) {
      setToken(res.data.access_token);
    }
    setAuthLoading(false);
  };

  // ── Generic endpoint tester ──
  const test = async (key, path, body) => {
    if (!token) return alert("Login first to get a token!");
    setLoading(key);
    const res = await apiFetch(path, body, token);
    setResults(r => ({ ...r, [key]: res }));
    setLoading("");
  };

  const endpoints = [
    {
      key:   "add",
      label: "POST /addWatchlist",
      color: "#1d3557",
      btnLabel: "▶ Add to Watchlist",
      fields: (
        <Field label="Movie ID" value={addId} onChange={setAddId} placeholder="e.g. 1" />
      ),
      run: () => test("add", "/movies/addWatchlist", { movieId: parseInt(addId) }),
    },
    {
      key:   "remove",
      label: "POST /movies/removeWatchList",
      color: "#6b2737",
      btnLabel: "▶ Remove from Watchlist",
      fields: (
        <Field label="Movie ID" value={removeId} onChange={setRemoveId} placeholder="e.g. 1" />
      ),
      run: () => test("remove", "/movies/removeWatchList", { movieId: parseInt(removeId) }),
    },
    {
      key:   "watched",
      label: "POST /markWatched",
      color: "#2d6a4f",
      btnLabel: "▶ Mark as Watched",
      fields: (
        <>
          <Field label="Movie ID" value={watchedId} onChange={setWatchedId} placeholder="e.g. 1" />
          <Field label="Rating (0.5–5)" value={rating} onChange={setRating} placeholder="3.5" />
          <Field label="Tag (optional)" value={tag} onChange={setTag} placeholder="e.g. great film" />
        </>
      ),
      run: () => test("watched", "/movies/markWatched", {
        movieId: parseInt(watchedId),
        rating:  parseFloat(rating),
        tags:    tag,
      }),
    },
  ];

  return (
    <div style={styles.page}>
      <h1 style={styles.title}>🎬 Watchlist API Tester</h1>
      <p style={styles.sub}>Testing: <code>{API}</code></p>

      {/* ── Auth Section ── */}
      <div style={styles.card}>
        <h2 style={styles.cardTitle}>Step 1 — Login to get JWT token</h2>
        <Field label="Email"    value={email}    onChange={setEmail}    placeholder="test@email.com" />
        <Field label="Password" value={password} onChange={setPassword} placeholder="Password1!" type="password" />
        <button style={{ ...styles.btn, background: "#444", marginTop: "0.5rem" }} onClick={login} disabled={authLoading}>
          {authLoading ? "Logging in..." : "▶ Login"}
        </button>

        {/* Token status */}
        <div style={{ marginTop: "0.75rem" }}>
          {token ? (
            <>
              <span style={styles.successBadge}>✓ Token received — ready to test</span>
              <div style={styles.tokenBox}>
                <code style={{ fontSize: "0.65rem", color: "#40916c", wordBreak: "break-all" }}>
                  {token}
                </code>
              </div>
            </>
          ) : (
            <span style={styles.emptyBadge}>No token yet — login first</span>
          )}
        </div>

        {/* Auth raw response */}
        {authResult && (
          <div style={{ marginTop: "0.75rem" }}>
            <p style={styles.sectionLabel}>Raw Response</p>
            <pre style={styles.pre}>{JSON.stringify(authResult.data, null, 2)}</pre>
          </div>
        )}
      </div>

      {/* ── Watchlist Endpoints ── */}
      <h2 style={{ ...styles.cardTitle, marginBottom: "1rem" }}>Step 2 — Test Watchlist Endpoints</h2>
      <div style={styles.grid}>
        {endpoints.map(({ key, label, color, btnLabel, fields, run }) => (
          <div key={key} style={{ ...styles.card, borderTop: `3px solid ${color}` }}>
            <h3 style={{ ...styles.cardTitle, color: "#ccc" }}>{label}</h3>
            {fields}
            <button
              style={{ ...styles.btn, background: color, marginTop: "0.5rem", opacity: token ? 1 : 0.4 }}
              onClick={run}
              disabled={loading === key || !token}
            >
              {loading === key ? "Testing..." : btnLabel}
            </button>

            {/* Result */}
            {results[key] && <ResultPanel result={results[key]} />}
          </div>
        ))}
      </div>
    </div>
  );
}

function Field({ label, value, onChange, placeholder, type = "text" }) {
  return (
    <>
      <label style={styles.label}>{label}</label>
      <input
        style={styles.input}
        type={type}
        value={value}
        onChange={e => onChange(e.target.value)}
        placeholder={placeholder}
      />
    </>
  );
}

function ResultPanel({ result }) {
  const success = result.ok;
  return (
    <div style={{ marginTop: "1rem", borderTop: "1px solid #2a2a2a", paddingTop: "0.75rem" }}>
      <div style={{ ...styles.badge, background: success ? "#40916c" : "#e63946", marginBottom: "0.75rem" }}>
        {success ? "✓ SUCCESS" : "✕ FAILED"} — HTTP {result.status}
      </div>

      {!success && (
        <p style={{ color: "#e63946", fontSize: "0.85rem", margin: "0 0 0.5rem" }}>
          {result.data.detail || JSON.stringify(result.data)}
        </p>
      )}

      <p style={styles.sectionLabel}>Raw Response</p>
      <pre style={styles.pre}>{JSON.stringify(result.data, null, 2)}</pre>
    </div>
  );
}

const styles = {
  page: {
    minHeight: "100vh",
    background: "#0f0f0f",
    color: "#f0f0f0",
    fontFamily: "monospace",
    padding: "2rem",
    maxWidth: "1100px",
    margin: "0 auto",
  },
  title: { fontSize: "1.8rem", marginBottom: "0.25rem" },
  sub:   { color: "#888", marginBottom: "2rem", fontSize: "0.85rem" },

  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(300px, 1fr))",
    gap: "1rem",
  },

  card: {
    background: "#1a1a1a",
    border: "1px solid #2a2a2a",
    borderRadius: "8px",
    padding: "1.25rem",
    marginBottom: "1.5rem",
    display: "flex",
    flexDirection: "column",
  },
  cardTitle: { margin: "0 0 0.75rem", fontSize: "0.95rem", color: "#aaa" },

  label: { fontSize: "0.72rem", color: "#777", marginBottom: "0.2rem" },
  input: {
    background: "#111",
    border: "1px solid #333",
    borderRadius: "6px",
    color: "#fff",
    padding: "0.55rem 0.75rem",
    fontSize: "0.9rem",
    outline: "none",
    marginBottom: "0.6rem",
    fontFamily: "monospace",
  },

  btn: {
    color: "#fff",
    border: "none",
    borderRadius: "6px",
    padding: "0.65rem 1rem",
    fontSize: "0.85rem",
    cursor: "pointer",
    fontFamily: "monospace",
    fontWeight: "bold",
  },

  badge: {
    display: "inline-block",
    padding: "0.2rem 0.65rem",
    borderRadius: "999px",
    fontSize: "0.72rem",
    fontWeight: "bold",
  },

  successBadge: {
    display: "inline-block",
    background: "#1a3d2b",
    color: "#40916c",
    padding: "0.2rem 0.65rem",
    borderRadius: "999px",
    fontSize: "0.72rem",
    marginBottom: "0.5rem",
  },
  emptyBadge: {
    display: "inline-block",
    background: "#2a2a2a",
    color: "#666",
    padding: "0.2rem 0.65rem",
    borderRadius: "999px",
    fontSize: "0.72rem",
  },

  tokenBox: {
    background: "#111",
    border: "1px solid #1a3d2b",
    borderRadius: "6px",
    padding: "0.5rem",
    marginTop: "0.4rem",
    maxHeight: "60px",
    overflowY: "auto",
  },

  sectionLabel: { fontSize: "0.68rem", color: "#666", textTransform: "uppercase", marginBottom: "0.3rem" },
  pre: {
    background: "#111",
    border: "1px solid #2a2a2a",
    borderRadius: "6px",
    padding: "0.65rem",
    fontSize: "0.75rem",
    color: "#ccc",
    overflowX: "auto",
    margin: 0,
  },
};
