# Py Core to Cloud

A Python-based foundation for building a **real-time multi-tenant chat service**. This project lays the groundwork for a Slack-style application with **web, mobile, and CLI clients**, focusing on clean architecture, automation, and developer experience.

---

## 🚀 Project Charter

The long-term goal is to deliver a **real-time chat service** that enables:

* Multi-organisation (tenant) support.
* Channel-based messaging for teams.
* File sharing and searchable message history.
* Real-time notifications across platforms.
* Unified clients for web, mobile, and CLI.

This repository is the **starting point**, with the backend and CLI bootstrap in Python, quality tools, and CI/CD.

---

## 📦 What’s Inside

* **Python backend skeleton** with CLI entrypoint (`py-core-to-cloud`).
* **uv-based build system** for fast, reproducible environments.
* **Developer tooling**:

  * [Ruff](https://github.com/astral-sh/ruff) – linting & formatting.
  * [Black](https://github.com/psf/black) – code formatting.
  * [Mypy](https://github.com/python/mypy) – static type checking.
  * [pytest](https://pytest.org) – testing framework.
* **Pre-commit hooks** for hygiene and style enforcement.
* **GitHub Actions CI** running tests and checks across Python 3.10–3.13.

---

## 🛠️ Getting Started

### Prerequisites

* Python **3.10+** (developed with 3.13).
* [uv](https://github.com/astral-sh/uv) for dependency and environment management.

### Installation

```bash
# Clone the repo
git clone https://github.com/<your-org>/py-core-to-cloud.git
cd py-core-to-cloud

# Sync dependencies (creates .venv automatically)
uv sync
```

### Running the CLI

```bash
uv run py-core-to-cloud --name Alice
# Output: Hello, Alice!
```

### Running Tests

```bash
uv run pytest -v
```

---

## 🗺️ Roadmap

### ✅ Foundation (Current)

* Project bootstrapping with `uv`, CLI, testing, linting, and CI.

### 🔜 MVP Features

* User authentication & multi-tenant support.
* Real-time messaging (WebSocket-based).
* Channel creation & management.

### 📂 Enhancements

* File uploads & storage integration.
* Searchable message history.

### 📱 Clients & UX

* Web client (React/Next.js).
* Mobile client (React Native/Flutter).
* CLI client expansion.

### 🔔 Advanced Features

* Push notifications.
* Admin dashboards & analytics.
* Third-party integrations (e.g., GitHub, Google Drive).

---

## 🤝 Contributing

Contributions are welcome!

* Open issues for bugs or feature ideas.
* Submit pull requests following the existing tooling and checks (`pre-commit`, `pytest`).

---

## 📄 License

This project is licensed under the [MIT License](./LICENSE).
