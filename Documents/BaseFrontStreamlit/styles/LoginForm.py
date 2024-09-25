from styles.BaseStyles import BaseStyles

class ContainerBt(BaseStyles):
    def __init__(self):
        self.target = ".stFormSubmitButton"

class AppView(BaseStyles):
    def __init__(self):
        self.target = '.st-emotion-cache-13ln4jf'

class Box2(BaseStyles):
    def __init__(self):
        self.target =  '.st-emotion-cache-1n76uvr'

class Box(BaseStyles):
    def __init__(self):
        self.target = '.st-emotion-cache-4uzi61'

class SubmitButton(BaseStyles):
    def __init__(self):
        self.target = '[data-testid="stBaseButton-secondaryFormSubmit"]'
        self.container = ContainerBt()
        
        
    def set_style(self):
        self.container.set_style()
        super().set_style()