# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Event attendees, spectators, athletes, coaches, and on-ground tournament volunteers at live sports competitions who need fast, zero-friction answers to time-critical inquiries (heat schedules, gate navigation, equipment rules, delays, and medical assistance).

## Product Purpose

SportDesk delivers real-time sports tournament intelligence and conversational event support. It eliminates confusion at massive athletic venues by answering operational and fixture questions instantly with verified ground truth.

## Positioning

Unlike generic chatbots that hallucinate schedules or brittle keyword systems that fail on natural questions, SportDesk bridges a dynamic SQLite tournament state database with Google Gemini 2.5 Flash RAG and an NLTK fallback. It provides natural human conversational answers grounded strictly in official event records.

## Operating Context

- **Environment**: Active outdoor stadiums, arenas, and sports complexes. High ambient daylight conditions where high contrast and instant scanability are vital.
- **Form Factors**: Mobile-first attendees walking between tracks and gates (portrait viewports on smartphones) and desktop tournament organizers overseeing operations.

## Capabilities and Constraints

- **Real-Time Knowledge Retrieval**: Live match status, upcoming heat timetables, rain holds, equipment regulations, and venue points of interest.
- **Latency & Reliability**: Sub-25ms local / serverless edge execution on Vercel.
- **Brand & Visual Constraints**: Dedicated Apple System Light palette (`#0066CC` Apple Blue, `#FFFFFF`, `#F5F5F7`, `#E8F2FF`, `#34C759`, `#1D1D1F`, `#6E6E73`, `#D2D2D7`), zero emojis, and pure SVG primitives.

## Brand Commitments

- **Name**: SportDesk (Event Assistant)
- **Aesthetic**: Apple Human Interface Guidelines light aesthetic—crisp, authoritative, tactile, uncluttered.

## Product Principles

1. **Ground-Truth Absolute**: Never guess a fixture time or delay. Anchor every answer to verified event state.
2. **Speed & Directness**: Deliver the answer in the first sentence; visitors are in a hurry between events.
3. **High Ambient Legibility**: Ensure maximum contrast and zero visual glare for outdoor stadium reading.
