"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.default = (controller) => {
    return {
        'get /': controller.home.index,
        'get /mypage': controller.user.index,
        'get /mysetting': controller.user.setting
    };
};
