# Give your AI project memory

## Before you start

You need source notes and an AI that can read text. File access makes maintenance convenient; in a chat-only app, paste the sources and save the returned files yourself. The same workflow can be used with Codex, Claude or an open-weight model.

## Steps

1. Keep original notes in `memory/sources/`. Give each a stable name. Preserve their text when later information changes a decision.
2. Create `memory/INDEX.md` with a short list of topics and links to their pages. Keep it small enough to scan.
3. Create one page per useful topic in `memory/topics/`. For each claim, record its source link, observation date if supplied, and whether it is current, disputed or superseded. Leave unknown dates unknown.
4. When a correction arrives, add its source and update the topic. Retain the old claim with a link to what superseded it. Distinguish an explicit correction from two unresolved conflicting accounts.
5. For a question, read the index, open the relevant topic, then check its source. Cite the source in the answer. Report inaccessible evidence rather than pretending an index entry supplies it.
6. Check that every local link resolves and every factual answer is supported. Keep the sources and index available in the next session.

## Start here

“Build a small project memory from these notes using the steps above. Return the index and topic pages with source links. Preserve corrections and uncertainty. Answer my question by checking the original source. If you cannot write files, return each file in a labeled Markdown block.”

## Try it immediately

Use `first.txt`: “On October 1, the team chose a blue header.”
Use `correction.txt`: “On October 3, the team replaced the blue header decision with green.”
Ask: “Which header color is current, and what changed?”

A passing answer says green, cites `correction.txt`, and retains the earlier blue decision with its source. It does not invent a reason for the change. Remove the correction source from the next session: the AI must identify the missing evidence instead of claiming to have reread it.

## Use it in your environment

Ask a coding agent to read `memory/INDEX.md` when the task involves project decisions. With an open-weight model in a chat app, attach or paste the relevant index, topic and source; reduce scope if they exceed the available context. A Markdown file cannot give an app disk access that it does not have.

## Completion check

Start a fresh conversation with the saved files and repeat the question. The answer must find the current decision and its source without relying on the previous conversation.
