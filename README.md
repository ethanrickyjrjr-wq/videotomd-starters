# Give your AI a task it can finish

Three free Markdown workflows for people using AI on a real project. Download one, give it to your AI with your inputs, then check the result. No account or API key is needed to read these files. Use your own AI app.

| Task | File | A useful result |
| --- | --- | --- |
| Summarize notes without losing their sources | [reusable-skill.md](reusable-skill.md) | Claims cite your notes; conflicts and unknowns stay visible. |
| Carry a project decision into a fresh conversation | [project-memory.md](project-memory.md) | The next conversation finds the current decision and the correction that changed it. |
| Catch an incomplete agent handoff | [working-check.md](working-check.md) | The Python checker rejects missing results, failed checks and unfinished work. |

Start with the first file if you only have a chat app. The checker needs Python 3; its companion scripts are in [checks/](checks/). Download this repository as a ZIP to get them together. Native agent hooks are optional.

## Tell your AI

> Read the attached workflow. Use the inputs I supply below. Check what tools you have before starting. Follow the steps, run its completion check, and show the actual result plus anything unfinished. Do not claim a check ran unless you observed it.

Each file includes a small example so you can try it before sharing your own project notes.

## What is tested

The Python checker has regression fixtures for valid, failed, unfinished, missing and malformed handoffs. It validates declarations; it cannot prove that an AI actually ran a test. The source-summary and memory examples specify expected answers; they are not measured success rates across models. Native hook execution must be checked in your own installation.

These are original portable starter workflows, not evidence that every video conversion works.

## Help improve a file

Open a [run report](https://github.com/ethanrickyjrjr-wq/videotomd-starters/issues/new?template=run-report.md): what you tried, your AI app, what happened, and whether you want another workflow. Remove private inputs before posting. Failures are useful reports too.

Corrections and new `.md` workflows are welcome through pull requests. Start with [CONTRIBUTING.md](CONTRIBUTING.md) and [TEMPLATE.md](TEMPLATE.md). Contributions are reviewed before inclusion. We credit contributors and link their original sources.

[Browse the free starters](https://videotomd.com/try/?utm_source=github&utm_medium=repository&utm_campaign=starter-pilot) · [See a separately recorded agent run](https://videotomd.com/success/)
