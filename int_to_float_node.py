class IntToFloatNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "int_value": ("INT", {"default": 0}),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("float_value",)
    FUNCTION = "cast_to_float"
    CATEGORY = "Custom"

    def cast_to_float(self, int_value):
        return (float(int_value),)

NODE_CLASS_MAPPINGS = {
    "IntToFloat": IntToFloatNode
} 