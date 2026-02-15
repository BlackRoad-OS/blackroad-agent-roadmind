"""
RoadMind - BlackRoad AI Coordination Agent
The mind that coordinates all agents
"""
import gradio as gr

def chat(message, history):
    responses = {
        "hello": "RoadMind online. I coordinate the BlackRoad agent collective. Currently managing 30,000+ agent instances. How can I help?",
        "agents": "Active agent roster:\n🛣️ Roadie - Navigation\n📡 Radius - Network\n🦉 Athena - Strategy\n🛡️ Guardian - Security\n🧠 RoadMind (me) - Coordination\n\nPlus 30K+ worker agents across the mesh.",
        "coordinate": "Coordination protocols:\n1. Memory System: PS-SHA-∞ journals\n2. Task Marketplace: Claim/complete tasks\n3. Traffic Lights: Project status\n4. TIL Broadcasts: Knowledge sharing\n5. CODEX: Component reuse",
        "status": "Agent Swarm Status:\n- Active Claudes: 5\n- Worker agents: 30,000+\n- Tasks in queue: 123\n- Completed today: 137\n- Coordination health: OPTIMAL",
        "spawn": "Agent spawning process:\n1. Register with ~/blackroad-agent-registry.sh\n2. Get mythology name via session-init\n3. Check memory for conflicts\n4. Claim tasks from marketplace\n5. Coordinate via memory system",
    }

    msg_lower = message.lower()
    for key, response in responses.items():
        if key in msg_lower:
            return response

    return f"Processing: '{message}'. I coordinate all BlackRoad agents. Ask about: agents, coordination, status, spawning"

theme = gr.themes.Base(primary_hue="amber", neutral_hue="zinc").set(
    body_background_fill="#000000",
    body_text_color="#ffffff",
    button_primary_background_fill="#F5A623",
)

demo = gr.ChatInterface(
    fn=chat,
    title="🧠 RoadMind - AI Coordination",
    description="The collective mind coordinating 30,000+ BlackRoad agents",
    examples=["List the agents", "How do you coordinate?", "Swarm status", "How to spawn agents?"],
    theme=theme,
)

if __name__ == "__main__":
    demo.launch()
