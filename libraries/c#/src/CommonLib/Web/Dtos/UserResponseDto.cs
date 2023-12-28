using System;
using System.ComponentModel.DataAnnotations;

namespace CommonLib.Web.Dtos
{
    public class UserResponseDto: IDto
    {
        public Guid? userId { get; internal set; }
        public string? userName { get; set; }
        public string? email { get; set; }
        public DateTime? dateTimeCreated { get; internal set; }
        public DateTime? dateTimeUpdated { get; internal set; }

        /// <summary>
        /// Method for validating member attributes
        /// </summary>
        /// <params></params>
        /// <returns>Returns IEnumerable<ValidationResult></returns>
        public IEnumerable<ValidationResult> Validate(ValidationContext validationContext)
        {
            throw new NotImplementedException();
        }
    }
}
