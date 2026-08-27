from agent.sensemaking.runtime import SensemakingAgent, Skill


def test_runtime_composes_skills():
    agent = SensemakingAgent()
    agent.register(Skill("double", lambda x: x * 2))
    agent.register(Skill("increment", lambda x: x + 1))

    assert agent.run(3, ["double", "increment"]) == 7
