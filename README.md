# codex_test
# AI Agent Development with Google Gemini

このリポジトリは，Google Gemini を利用した AI エージェントの開発用です．
まず仮想環境を構築し，段階的に機能を追加していきます．

---

## 開発環境の準備

### 1. 仮想環境の作成
Python 3.10 以降を推奨します．

### 2. API キーの設定
1. `.env.example` を `.env` にコピーし，`GEMINI_API_KEY` を設定します．
2. `.env` は `.gitignore` によりリポジトリにコミットされません．

```bash
cp .env.example .env
```

### 3. テストの実行

```bash
pytest
```
