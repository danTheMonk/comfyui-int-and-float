import math

class FloatToIntNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "float_value": ("FLOAT", {"default": 0.0}),
                "rounding_mode": (["down (floor)", "up (ceil)"], {"default": "down (floor)"}),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("int_value",)
    FUNCTION = "cast_to_int"
    CATEGORY = "Custom"

    def cast_to_int(self, float_value, rounding_mode):
        if rounding_mode == "up (ceil)":
            return (int(math.ceil(float_value)),)
        else:
            return (int(math.floor(float_value)),)

NODE_CLASS_MAPPINGS = {
    "FloatToInt": FloatToIntNode
} 