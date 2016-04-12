import bpy
from bpy.props import *
from ... events import executionCodeChanged
from ... base_types.node import AnimationNode

caseTypeItems= [("UPPER", "To Upper Case", ""),
                ("LOWER", "To Lower Case", ""),
                ("CAPITALIZE", "Capitalize Phrase", ""),
                ("CAPITALIZE_WORDS", "Capitalize Words", "") ]

caseTypeCode = { item[0] : item[0].lower() for item in caseTypeItems }

class ChangeTextCaseNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_ChangeTextCaseNode"
    bl_label = "Change Text Case"

    def caseTypeChanges(self, context):
        executionCodeChanged()

    caseType = EnumProperty(
        name = "Case Type", default = "CAPITALIZE",
        items = caseTypeItems, update = caseTypeChanges)

    def create(self):
        self.newInput("String", "Text", "inText")
        self.newOutput("String", "Text", "outText")

    def draw(self, layout):
        layout.prop(self, "caseType", text = "")

    def getExecutionCode(self):
        if self.caseType == "CAPITALIZE_WORDS":
            return "outText = ' '.join( [t.capitalize() for t in inText.split()])"
        return "outText = inText.{}()".format(caseTypeCode[self.caseType])
